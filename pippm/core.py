def main():
    try:

        import argparse

    except ImportError as error:

        print("pippm failed, could not import required modules.\nError: {0}".format(error))

    else:

        parser = argparse.ArgumentParser(description="A utility for managing pip packages")

        parser.add_argument("name", help="The name of the package")

        parser.add_argument("action", help="The action to be performed.", choices=["init", "test", "deploy", "remove", "environment", "transpile", "build"], default="init")
        
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

        elif args.action == "transpile":

            transpile(args)

def initialize(args):

    try:

        import json, os, venv

    except ImportError as error:

        print("Initialization failed, could not import required packages. \n Error: {0}".format(error))

    else:

        location = args.location if args.location else os.path.join(os.getcwd(), args.name)

        print("Are you sure you want to create this package? ({0})".format(args.name))

        response = input("Y for yes, N for no.").upper()

        if response == "Y" or response == "YES":
            
            print("Creating package... {0}\nLocation: \n\t{1}".format(args.name, location))

            for directory in ["sources", "builds", "include", "environments", "tests", "examples"]:

                try:

                    os.makedirs(os.path.join(location, directory))

                    for language in ["Python", "JavaScript", "C", "C++", "C#", "F#", "Perl", "Bash", "Java", "Assembler", "Visual Basic"]:

                        try:
                            os.makedirs(os.path.join(location, directory, language))
                        except OSError as e:
                            print("Existing directory: \n\t{0}".format(os.path.join(location, directory, language)))

                except OSError as e:

                    print("Existing directory: \n\t{0}".format(os.path.join(location, directory)))

            with open(os.path.join(location, ".gitignore"), "a+") as gitignore:

                print("__pycache__", file=gitignore)
                print(".pypirc", file=gitignore)
                print("environments", file=gitignore)

            with open(os.path.join(location, "sources", "Python", "requirements.txt"), "a+") as requirements:

                pass

            with open(os.path.join(location, "sources", "Python", "package.json"), "w+") as packageJson, open(os.path.join(location, "sources", "Javascript", "package.json"), "w+") as nodePackage:

                print("A package.json file will now be created for you.")

                nameInput = input("package name: ({0})".format(args.name)).strip() or args.name
                versionInput = input("version: (1.0.0)").strip() or "1.0.0"
                descriptionInput = input("description: ").strip()
                entryPointInput = input("entry point: (__main__.py)").strip() or "__main__.py"
                testCommandInput = input("test command: (\"echo \\\"Error: no test specified\" && exit 1\")").strip() or "\"echo \\\"Error: no test specified\" && exit 1\""
                gitRepositoryInput = input("git repository: ").strip()
                keywordsInput = input("keywords: ").strip()
                authorInput = input("author: ({0})".format(os.getlogin())).strip() or os.getlogin()
                licenseInput = input("license: ").strip()

                packageDictionary = {
                    "name": nameInput,
                    "version": versionInput,
                    "description": descriptionInput,
                    "main": entryPointInput,
                    "directories": {"test": "tests"},
                    "scripts": {"test": testCommandInput},
                    "repository": {
                        "type": "git",
                        "url": "git+{0}.git".format(gitRepositoryInput)
                    },
                    "keywords": [keyword for keyword in keywordsInput.split(" ")],
                    "author": authorInput,
                    "bugs": {
                        "url": "{0}/issues".format(gitRepositoryInput)
                    },
                    "homepage": "{0}#readme".format(gitRepositoryInput)
                }

                packageJson.write(json.dumps(packageDictionary))

            builderInst = venv.EnvBuilder()

            builderInst.create(os.path.join(location, "environments", args.name))

        else:
            
            print("User canceled package creation. Package {0} was not created.".format(args.name))

    #Initialization code here

def getSystemInfo():
    try:
        import os, platform, sys, struct
    except ImportError as e:
        print("could not get system info. \nError: {0}".format(e))
    else:
        return {
            "operatingSystem": sys.platform,
            "bitness": "{0}bit".format(8 * struct.calcsize("P")),
            "platformInfo": platform.platform(),
            "python": {
                "fullVersion": sys.version,
                "version": sys.version_info
            }
        }
    pass
    #return a dictionary representing the information on the operatring system, bitness and etc for other parts of the program to use

def test():
    pass
    #install code here

def deploy():
    pass
    #uninstall code here

def remove():
    pass
    #test code here

def environment():
    #environment creation here; if the environment with a matching signature (python version, subversion and platform archetecture) exists, inform the user and ask "overwrite?"
    pass

def build():
    #build instructions here... if the user's platform is Microsoft we can probably try to py2exe... otherwise try to freeze the modules (py2exe for unix)
    pass

#subprocess.call("py -m venv {0}".format())
