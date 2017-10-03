from . import core

async def main():
    """The main function to be run when pippm is run from the command line"""
    try:

        import argparse

    except ImportError as error:

        print("pippm failed, could not import required modules.\nError: {0}".format(error))

    else:

        parser = argparse.ArgumentParser(description="A utility for managing pip packages")

        subparsers = parser.add_subparsers(help="Action-specific help menu")

        parser_init = subparsers.add_parser('init', help="Initialize the package with directories, files and package.json(s)")
        parser_init.add_argument('--location', '-l', help="The location to initialize the directory at", required=False)
        parser_init.set_defaults(func=init)

        parser_test = subparsers.add_parser('test', help="Perform a named test in a package")
        parser_test.add_argument('name', help="The name of the test you wish to perform, must have the same name in package.json")
        parser_test.add_argument('--location', '-l', help="The path to the directory containing the test to run", required=False)
        parser_test.set_defaults(func=test)

        parser_deploy = subparsers.add_parser('deploy', help="Deploy the code to a package manager")
        parser_deploy.add_argument('--language', '-p', help="The programming language to deploy, javascript or js for JavaScript (npm) and python or py for Python (pip)", choices=['javascript', 'js', 'python', 'py'], required=True)
        parser_deploy.add_argument('--location', '-l', help="Where the code you wish to deploy exists", required=False)
        parser_deploy.set_defaults(func=deploy)

        parser_remove = subparsers.add_parser('remove', help="Remove a package from your machine (basically deletes the directory, nothing wrong with manually removing them either)")
        parser_remove.add_argument('--location', '-l', help="The location of the package you wish to remove", required=False)
        parser_remove.add_argument('--recursive', '-r', help="Changes the behaviour of the program to search recursively for packages and remove them", required=False)
        parser_remove.add_argument('--silent', '-s', help="WARNING: Program will not ask you for permission before trying to delete the file!", action='store_true')
        parser_remove.set_defaults(func=remove)

        parser_environment = subparsers.add_parser('environment', help="Add a platform environment to the package")
        parser_environment.add_argument('--location', '-l', help="The path to the package to add the environment to", required=False)
        parser_environment.add_argument('--recursive', '-r', help="Changes the behaviour of the program to search recursively for packages and add the environment to them", required=False)
        parser_environment.add_argument('--silent', '-s', help="WARNING: Program will not ask for your permission before adding environments!", action='store_true')
        parser_environment.set_defaults(func=environment)

        parser_transpile = subparsers.add_parser('transpile', help="Convert the source code from one language to another")
        parser_transpile.add_argument('--location', '-l', help="The directory where the package to be transpiled is located", required=False)
        parser_transpile.add_argument('--source', '-s', help="The source language", required=False, choices=["javascript", "js", "python", "py"], default="python")
        parser_transpile.add_argument('--destination', '-d', help="The destination language", required=False, choices=["javascript", "js", "python", "py"], default="javascript")
        parser_transpile.set_defaults(func=transpile)

        parser_build = subparsers.add_parser('build', help="Py2exe or freeze the package python code")
        parser_build.add_argument('--location', '-l', help="The directory where the package to be built exists", required=False)
        parser_build.set_defaults(func=build)

        #parser.add_argument("action", help="The action to be performed.", choices=["init", "test", "deploy", "remove", "environment", "transpile", "build"], default="init")
        
        #parser.add_argument("--testname", "-t", help="The test to run.", required=False)

        #parser.add_argument("--location", "-l", help="The location to create the package at.", required=False)

        args=parser.parse_args()

        args.func(args)

async def init(args):
    """
    Run core.initialize appropriately
        :param args: The arguments from the termainal
    """
    await core.initialize(location=args.location)

async def test(args):
    """
    Run core.test appropriately
        :param args: The arguments from the terminal
    """
    await core.test(testname=args.name, location=args.location)
    
async def deploy(args):
    """
    Run core.deploy appropriately
        :param args: The arguments from the terminal
    """
    await core.deploy(location=args.location)

async def remove(args):
    """
    Run core.remove appropriately
        :param args: The arguments from the terminal
    """
    await core.remove(location=args.location)


async def environment(args):
    """
    Run core.environment appropriately
        :param args: The arguments from the terminal
    """
    await core.environment(location=args.location)

async def transpile(args):
    """
    Run core.transpile appropriately
        :param args: The arguments from the terminal
    """
    await core.transpile(location=args.location)

async def build(args):
    """
    Run core.build appropriately
        :param args: The arguments from the terminal
    """
    await core.build(location=args.location)

try:
    import asyncio
except ImportError as e:
    print("Could not import async lib\nError: {0}".format(e))
else:
    
    #initialize asynchronous loop
    loop = asyncio.get_event_loop()

    #run the main function
    loop.run_until_complete(main())