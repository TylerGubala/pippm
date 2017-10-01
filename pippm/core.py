def main():
    try:

        import argparse

    except ImportError as error:

        print("pippm failed, could not import required modules.\nError: {0}".format(error))

    else:

        parser = argparse.ArgumentParser(description="A utility for managing pip packages")

        parser.add_argument("name", help="The name of the package")

        parser.add_argument("--action", "-a", help="The action to be performed.", choices=["init", "test", "deploy", "remove"], default="init")
        
        parser.add_argument("--testname", "-t", help="The test to run.", required=False)

        parser.add_argument("--location", "-l", help="The location to create the package at.", required=False)

        args=parser.parse_args()

        if args.action == "init":

            initialize(args)

        elif args.action == "test":

            test(args)

        elif args.action == "deploy":

            deploy(args)

        elif args.action == "remove":

            remove(args)

def initialize(args):

    try:

        import json, os, venv

    except ImportError as error:

        print("Initialization failed, could not import required packages. \n Error: {0}".format(error))

    else:

        location = args.location if args.location else os.path.join(os.getcwd(), args.name)

        print("Are you sure you want to create this package? ({0})".format(args.name))

        if input("Y for yes, N for no.").upper() is "Y" or "YES":
            
            print("Creating package... {0}\nLocation: \n\t{1}".format(args.name, location))

            for directory in ["sources", "builds", "include", "environments", "tests"]:

                try:

                    os.makedirs(os.path.join(location, directory))

                except OSError as e:

                    print("Existing directory: \n\t{0}".format(os.path.join(location, directory)))

            with open(os.path.join(location, ".gitignore"), "a+") as gitignore:

                print("__pycache__", file=gitignore)
                print(".pypirc\n", file=gitignore)
                print("environments\n", file=gitignore)

            with open(os.path.join(location, "requirements.txt"), "a+") as requirements:

                pass

            with open(os.path.join(location, "package.json"), "a+") as npmlike:

                print("A package.json file will now be created for you.")

                nameInput = input("package name: ({0})".format(args.name)).strip()
                versionInput = input("version: (1.0.0)")
                descriptionInput = input("description: ")
                entryPointInput = input("entry point: ({0})")
                testCommandInput = input("test command: (\"echo \\\"Error: no test specified\" && exit 1\")")
                gitRepositoryInput = input("git repository: (\"\")")
                

                npmdict = {
                    "name": args.name
                    "version": 
                }

                pass

            builderInst = venv.EnvBuilder()

            builderInst.create(os.path.join(location, "environments", args.name))

        else:
            
            print("User canceled package creation. Package {0} was not created.".format(args.name))

    #Initialization code here

def test():
    pass
    #install code here

def deploy():
    pass
    #uninstall code here

def remove():
    pass
    #test code here

#subprocess.call("py -m venv {0}".format())
