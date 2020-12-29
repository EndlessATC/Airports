import argparse
import os
import re

def main(args, input_file=None):
	pattern = re.compile(r"^(?P<airport_section>\[airport(?P<airport_id>\d*)\])|(?P<airline_entry>#!\t(?P<airline_code>[-\w]*), (?P<airline_frequency>\d*), (?P<airline_parameters>[\w/d]*, [-\w ]*, [nswe]*))|(?P<result_marker>#!expansionoutput(?P<result_id>\d+))|(?P<result_end_marker>#!expansionoutputend)|(?P<sid_marker>#!sid(?P<sid_frequency>[\d]+)x)")
	
	result = {'output': []}
	airport = 0
	ignore_lines = False
	ignore_one_line = False
	sid_frequency = 0
	sid_lines = []
	if input_file is None:
		input_file = args.input_file
		output_file = input_file if args.output_file is None else args.output_file
	else:
		output_file = os.path.join(os.path.dirname(input_file), args.output_path, os.path.basename(input_file))
	print("Building {0} to {1}".format(input_file, output_file))

	with open(input_file, 'r', newline='') as airport_file:
		for line in airport_file:
			match = pattern.match(line)
			if match:
				if match['airport_section']:
					airport = match['airport_id']
					if not airport in result:
						result[airport] = []

				elif match['airline_entry']:
					total_frequency = int(match['airline_frequency'])
					frequencies = []
					while total_frequency > 10:
						frequencies.append(10)
						total_frequency -= 10
					frequencies.append(total_frequency)
					for frequency in frequencies:
						result[airport].append("\t{match[airline_code]}, {frequency}, {match[airline_parameters]}\n".format(match=match, frequency=frequency))

				elif match['result_marker']:
					result['output'].append(line)
					for result_line in result[match['result_id']]:
						result['output'].append(result_line)
					ignore_lines = True

				elif match['result_end_marker']:
					ignore_lines = False

				elif match['sid_marker']:
					sid_frequency = int(match['sid_frequency']) - 1
					ignore_one_line = True

			if sid_frequency:
				if line.isspace():
					for _ in range(sid_frequency):
						result['output'].extend(sid_lines)
					sid_frequency = 0
					sid_lines = []
				elif not len(sid_lines):
					sid_lines.append("\n")
				else:
					sid_lines.append(line)

			if not ignore_lines and not ignore_one_line:
				result['output'].append(line)

			if ignore_one_line:
				ignore_one_line = False

	with open(output_file, 'w', newline='') as airport_file:
		airport_file.writelines(result['output'])
	return output_file

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='''Expands certain commands to allow for concise Endless ATC airport source files. 

		#!expansionoutput<airport_id> can be inserted on its own line in a source file terminated by 
		#!expansionoutputend on a following line. This block, which should remain empty, will be used
		to write the result of expanding any airline definitions in a #! comment. Any #! definitions
		with frequency greater are split into entries with max 10 frequency each.

		#!sid<n>x can be inserted before any "routex =" declaration in a [departure] section to repeat the
		route <n> times. This can be used to adjust the distribution of traffic on each SID. Note the
		numbering of each "route" will not be adjusted. See renumber.py for such operation.''')
	parser.add_argument('input_file')
	parser.add_argument('output_file', nargs='?')

	main(parser.parse_args())