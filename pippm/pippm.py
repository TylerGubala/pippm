def main():
    try:

        import argparse

    except ImportError as error:

        print("pippm failed, could not import required modules.\nError: {0}".format(error))

    else:

        parser = argparse.ArgumentParser(
            description="""A package manager tool for python.\n
            Includes:\n
            \t-automatic virtual environment creation\n
            \t-automatic tracking of packages as they are installed\n
            \t-helpers for pip (creation of .pypirc and addition of .pypirc to .gitignore)""",
            formatter_class=argparse.RawTextHelpFormatter
            )

        parser.add_argument("name", help="The name of the package")
        
        group = parser.add_mutually_exclusive_group()

        group.add_argument("--init", "-n", help="Create the virtual environment named after the package", action="store_true")

        group.add_argument("--remove", "-r", help="Remove package and associated virtual environment", action="store_true")

        group.add_argument("--install", "-i", help="Using pip, install a dependency at the named package", action="store_true")

        group.add_argument("--uninstall", "-u", help="Using pip, uninstall a dependency at the named package", action="store_true")

        parser.add_argument("--dependency", help="The name of the dependency to install/uninstall", required=parser.parse_args().uninstall or parser.parse_args().install)

        args=parser.parse_args()

        if args.init:

            initialize(args)

def initialize(args):

    try:

        import asyncio, json, os, venv

    except ImportError as error:

        print("Initialization failed, could not import required packages. \n Error: {0}".format(error))

    else:

        print("Are you sure you want to create this package? ({0})".format(args.name))

        if input("Y for yes, N for no.").upper() is "Y" or "YES":
            
            print("Creating package... {0}".format(args.name))
            
        else:
            
            print("User canceled package creation. Package {0} was not created.".format(args.name))

    #Initialization code here

def install():
    pass
    #install code here

def uninstall():
    pass
    #uninstall code here

def test():
    pass
    #test code here

#subprocess.call("py -m venv {0}".format())