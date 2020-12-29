import argparse
import configparser
import glob
import os
import shutil

config = configparser.ConfigParser()
config.read('eatcdev.ini')
default_destination = config['deploy'].get("path", "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Endless ATC\\locations\\") if 'deploy' in config else "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Endless ATC\\locations\\"

def main(args):
	if args.build:
		import expand
		import renumber

	destination = args.destination_path or default_destination
	if args.deploy:
		print(f"Deploying to {args.destination_path or destination}.")

	if not args.codes:
		import distutils.util
		if not distutils.util.strtobool(input("Confirm you wish to process all airport files? (y/n) ")):
			print("Aborting.")
			return
		args.codes.append("")

	for code in args.codes:
		path = os.path.join(args.input_dir, "**", args.source_dir, args.pattern.format(code = code))
		for file in glob.glob(path, recursive=True):
			print(f'Found {file}')
			if args.build:
				file = expand.main(args, file)
				renumber.main(args, file)
			if args.deploy:
				result = shutil.copy(file, destination)
				print(f"Copied {file} to {result}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Build specified Endless ATC airports and copy to the Endless ATC directory.", epilog="https://github.com/AdamJCavanaugh/EndlessATCAirports")
	parser.add_argument('codes', nargs='*', help="Airport codes to build and deploy. Prefixes can be used. If no code specified, you will be prompted if all airport files are to be processed.", metavar="code")
	parser.add_argument('-w', '--input-dir', default=os.path.join(os.pardir, 'final'), help='''The directory containing the airport files. 
		Subdirectories that are not source directories will also be searched. Defaults to '../final'.''')
	parser.add_argument('-s', '--source-dir', default='source', help="The name of the folders that will contain source files. Defaults to 'source'.")
	parser.add_argument('-p', '--pattern', default='{code}*.txt', help="The glob pattern for the file names to build based on the input codes. Defaults to '{code}*.txt'.")
	parser.add_argument('-o', '--output-path', default=os.pardir, help='''The path to the directory to store the output of the build process relative to the source file. 
		Defaults to the parent directory relative to the source file.''')
	parser.add_argument('-d', '--destination-path', help='''The directory to copy the output of the build process to (e.g. Endless ATC locations folder). 
		Defaults to "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Endless ATC\\locations\\".
		This default can be overridden by a 'path = ' entry under a [deploy] section in an eatcdev.ini.''')
	parser.add_argument('-n', '--no-build', action='store_false', dest='build', help='Specify to skip build, and just copy sources to output folder.')
	parser.add_argument('-b', '--build-only', action='store_false', dest='deploy', help="Specify this option to skip copying output of build processes to destination folder.")

	main(parser.parse_args())
