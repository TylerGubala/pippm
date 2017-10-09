"""Core functionality to pippm is contained in this submodule"""
import aiofiles, git, json, os, platform, struct, subprocess, sys, venv

from pip.operations.freeze import freeze

from typing import Optional, List, Dict

async def initialize(location: Optional[str] = os.getcwd(), languages: Optional[List[str]] = ["Python", "Javascript"]) -> None:
    """
    Initialize a pippm package at the location specified
        :param location (str): Path to create the new package (default: the current working directory)
        :param languages (List[str]): The languages to create directories for (you can always add more languages later)
        :return (None): Does not return anything. If an exception is raised something went wrong, otherwise everything is fine.
    """

    location = location if location is not None else os.getcwd()

    print("Are you sure you want to create a package at:\n\t{0}".format(location))

    response = input("Y for yes, N for no.").upper()

    if response == "Y" or response == "YES":
            
        print("Creating package... \nLocation: \n\t{0}".format(location))

        await initializeStructure(location=location, languages=languages)

    else:
            
        print("User canceled package creation. Package was not created.")

    #Initialization code here


async def test(testname: str, location: Optional[str] = os.getcwd()) -> None:
    """
    Run a named test
        :param testname (str): The test to run - required
        :param location (str): The path to the package containing the named test (default: the current working directory)
        :return (None): Does not return anything. If an exception is raised something went wrong, otherwise everything is fine.
    """
    pass
    #Test code here

async def deploy(location: Optional[str] = os.getcwd()) -> None:
    """
    Deploy the package to the setup script
        :param location (str): The location of the package that is to be deployed (default: the current working directory)
        :return (None): Does not return anything. If an exception is raised something went wrong, otherwise everything is fine.
    """
    pass
    #Deploy code here

async def remove(location: Optional[str] = os.getcwd()) -> None:
    """
    Remove a package from the user's system
        :param location (str): The location of the package to remove; basically the directory to delete (but only if a package manifest sits at the root of that directory) (default: the current working directory)
        :return (None): Does not return anything. If an exception is raised something went wrong, otherwise everything is fine.
    """
    pass
    #test code here

async def environment(location: Optional[str] = os.getcwd()) -> None:
    """
    Add an environment to the package (especially for Microsoft, Macintosh or Linux distributions which vary greatly)
        :param location (str): The package to make the environment (default: the current working directory)
        :return (None): Does not return anything. If an exception is raised something went wrong, otherwise everything is fine.
    """
    #environment creation here; if the environment with a matching signature (python version, subversion and platform archetecture) exists, inform the user and ask "overwrite?"

    builderInst = venv.EnvBuilder()

    systemInfo = await getSystemInfo()

    builderInst.create(os.path.join(location, "environments", "Python", systemInfo["operatingSystem"], "{0}.{1}.{2} {3}".format(systemInfo["python"]["version"][0], systemInfo["python"]["version"][1], systemInfo["python"]["version"][2], systemInfo["bitness"])))

async def build(location: Optional[str] = os.getcwd()) -> None:
    """
    Make an executable from the packge code (py2exe, freeze, etc, platform dependent)
        :param location (str): The location of the package containing the code to build (default: the current working directory)
        :return (None): Does not return anything. If an exception is raised something went wrong, otherwise everything is fine.
    """
    #build instructions here... if the user's platform is Microsoft we can probably try to py2exe... otherwise try to freeze the modules (py2exe for unix)
    pass
async def getSystemInfo() -> Dict:
    """
    Return a python dictionary describing the system and python platform
        :return (Dict): Returns a dictionary representing the system configuration.
    """

    return {
        "operatingSystem": sys.platform,
        "bitness": "{0}bit".format(8 * struct.calcsize("P")),
        "platformInfo": platform.platform(),
        "python": {
            "fullVersion": sys.version,
            "version": sys.version_info
        }
    }
    #return a dictionary representing the information on the operatring system, bitness and etc for other parts of the program to use

async def getDependencies() -> Dict:  
    pass  

async def initializeStructure(location: str = os.getcwd(), languages: List[str] = ["Python", "Javascript"]) -> None:
    """
    Set up files and folders
        :param location (str): The location of the package to set up files and folders (default: the current working directory)
        :param languages (List[str]): The language specific directories to create for sources, etc (default ["Python", "Javascript"])
        :return (None): Does not return anything. If an exception is raised something went wrong, otherwise everything is fine.
    """

    location = location if location is not None else os.getcwd()

    for directory in ["sources", "builds", "include", "environments", "tests", "examples"]:

        try:

            os.makedirs(os.path.join(location, directory))

            for language in languages:

                try:
                    os.makedirs(os.path.join(location, directory, language))
                except OSError as e:
                    print("Existing directory: \n\t{0}".format(os.path.join(location, directory, language)))

        except OSError as e:

            print("Existing directory: \n\t{0}".format(os.path.join(location, directory)))

    async with aiofiles.open(os.path.join(location, "sources", "Python", "requirements.txt"), "w+") as requirements:

        pass

    print("A package.json file will now be created for you.")

    nameOfThePackage = os.path.basename(os.path.normpath(location))

    nameInput = input("package name: ({0})".format(nameOfThePackage)).strip() or nameOfThePackage
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
        "directories": {"test": "../../tests"},
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

    async with aiofiles.open(os.path.join(location, "sources", "Python", "package.json"), "w+") as packageJson, aiofiles.open(os.path.join(location, "sources", "Javascript", "package.json"), "w+") as nodePackage:

        await packageJson.write(jsonString)
        await nodePackage.write(jsonString)

    await environment(location)

    git.Repo.init(location)

    async with aiofiles.open(os.path.join(location, ".gitignore"), "w+") as gitignore:

        await gitignore.write('\n'.join(["__pycache__", "environments", ".pypirc"]))

    try: 
        os.makedirs(os.path.join(location, "sources", "Python", nameInput))
    except OSError as e:
        print("Existing directory: \n\t{0}".format(os.path.join(location, directory, language)))

    async with aiofiles.open(os.path.join(location, "sources", "Python", nameInput, "__init__.py"), "w+") as initpy, aiofiles.open(os.path.join(location, "sources", "Python", nameInput, entryPointInput), "w+") as entrypoint:

        await initpy.write('"""{packageDescription}"""'.format(packageDescription=descriptionInput))
        await entrypoint.write('"""{packageName} entry point\nTODO: Add package code"""'.format(packageName=nameInput, file=entrypoint))

    async with aiofiles.open(os.path.join(location, "sources", "Python", "setup.py"), "w+") as setuppy:

        await setuppy.write('\
\n"""set-up script"""\n\
import json\n\
from setuptools import setup\n\
\n\
with open("package.json", "r") as packageJsonFile:\n\
    packageJson=json.loads(packageJsonFile.read())\n\
setup(\n\
    name = packageJson.name,\n\
    version = packageJson.version,\n\
)')