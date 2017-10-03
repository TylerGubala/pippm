"""Core functionality to pippm is contained in this submodule"""
async def initialize(location=None):
    """
    Initialize a pippm package at the location specified
        :param location=None: Path to create the new package
    """
    try:

        import json, os, venv

    except ImportError as error:

        print("Initialization failed, could not import required packages. \n Error: {0}".format(error))

    else:

        location = location if location is not None else os.getcwd()

        print("Are you sure you want to create a package at:\n\t{0}".format(location))

        response = input("Y for yes, N for no.").upper()

        if response == "Y" or response == "YES":
            
            print("Creating package... \nLocation: \n\t{0}".format(location))

            await initializeStructure(location=location)

        else:
            
            print("User canceled package creation. Package was not created.")

    #Initialization code here


async def test(testname, location=None):
    """
    Run a named test
        :param testname: The test to run
        :param location=None: The path to the package containing the named test. If not specified, look for a package at the CWD
    """
    pass
    #Test code here

async def deploy(location=None):
    """
    Deploy the package to the setup script
        :param location=None: The location of the package that is to be deployed
    """
    pass
    #Deploy code here

async def remove(location=None):
    """
    Remove a package from the user's system
        :param location=None: The location of the package to remove; basically the directory to delete (but only if a package manifest sits at the root of that directory)
    """
    pass
    #test code here

async def environment(location=None):
    """
    Add an environment to the package (especially for Microsoft, Macintosh or Linux distributions which vary greatly)
        :param location=None: The package to make the environment
    """
    #environment creation here; if the environment with a matching signature (python version, subversion and platform archetecture) exists, inform the user and ask "overwrite?"
    pass

async def build(location=None):
    """
    Make an executable from the packge code (py2exe, freeze, etc, platform dependent)
        :param location=None: The location of the package containing the code to build
    """
    #build instructions here... if the user's platform is Microsoft we can probably try to py2exe... otherwise try to freeze the modules (py2exe for unix)
    pass
async def getSystemInfo():
    """
    Return a python dictionary describing the system and python platform
    """
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

async def initializeStructure(location=None):
    """
    Set up files and folders
        :param location=None: The location of the package to set up files and folders
    """
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
            "directories": {"test": "../tests"},
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

        jsonString = json.dumps(packageDictionary)
        print(jsonString, file=packageJson)
        print(jsonString, file=nodePackage)

    builderInst = venv.EnvBuilder()

    builderInst.create(os.path.join(location, "environments", args.name))