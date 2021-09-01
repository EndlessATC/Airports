import argparse
import configparser
import glob
import os
import shutil

"""Endless ATC custom airport file deployment utility.

Can build from source and deploy to game folder in one step.

See argparse help for details."""

config = configparser.ConfigParser()
config.read('eatcdev.ini')
if 'deploy' not in config:
    config.add_section('deploy')
default_destination = config['deploy'].get(
    "path",
    "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Endless ATC\\locations\\"
)


def main(args):
    """Builds an Endless ATC custom airport source file and deploys the built file
    to the game folder.

    Refer to argparse help for details.

    Args:
        `args`: An `argparse.Namespace`. The command line args when invoked as a module."""

    if args.build:
        import expand
        import renumber

    destination = args.destination_path or default_destination
    if args.deploy:
        print(f"Deploying to {args.destination_path or destination}.")

    if not args.codes:
        from distutils.util import strtobool
        if not strtobool(input("Confirm you wish to process all airport files? (y/n) ")):
            print("Aborting.")
            return
        args.codes.append("")

    for code in args.codes:
        path = os.path.join(
            args.input_dir,
            "**",
            args.source_dir,
            args.pattern.format(code=code))
        for file in glob.glob(path, recursive=True):
            print(f'Found {file}')
            if args.build:
                preprocess = renumber.process(args, file)
                file = expand.process(args, file, preprocess)
            if args.deploy and not args.parse_only:
                result = shutil.copy(file, destination)
                print(f"Copied {file} to {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build specified Endless ATC airports and copy to the Endless ATC directory.",
        epilog="https://github.com/AdamJCavanaugh/EndlessATCAirports")
    parser.add_argument('codes', nargs='*', metavar="code",
        help='''Airport codes to build and deploy. Prefixes can be used.
        If no code specified, you will be prompted if all airport files are to be processed.''')
    parser.add_argument('-w', '--input-dir',
        default=os.path.join(os.pardir, 'final'),
        help='''The directory containing the airport files.
        Subdirectories that are not source directories will also be searched.
        Defaults to '../final'.''')
    parser.add_argument('-s', '--source-dir', default='source',
        help='''The name of the folders that will contain source files.
        Defaults to 'source'.''')
    parser.add_argument('-p', '--pattern', default='{code}*.txt',
        help="The glob pattern for the file names to build based on the input codes. Defaults to '{code}*.txt'.")
    parser.add_argument('-o', '--output-path', default=os.pardir,
        help='''The path to the directory to store the output of the build process relative to the source file.
        Defaults to the parent directory relative to the source file.''')
    parser.add_argument('-d', '--destination-path',
        help='''The directory to copy the output of the build process to (e.g. Endless ATC locations folder).
        Defaults to "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Endless ATC\\locations\\".
        This default can be overridden by a 'path = ' entry under a [deploy] section in an eatcdev.ini.''')
    parser.add_argument('-n', '--no-build', action='store_false', dest='build',
        help='Specify to skip build, and just copy sources to output folder.')
    parser.add_argument('-b', '--build-only',
        action='store_false', dest='deploy',
        help="Specify this option to skip copying output of build processes to destination folder.")
    parser.add_argument('-P', '--parse-only', action='store_true',
        help="Do not write any output of build. Also has effect of --build-only.")
    parser.add_argument('-t', '--test-callsigns', action = 'store_true',
        help="Tests loading of shared callsigns. Actual output is not based on shared callsigns.")
    parser.add_argument('-a', '--draw-all-areas', action = 'store_true',
        help="Ignore draw= in [area]s while building.")

    main(parser.parse_args())
