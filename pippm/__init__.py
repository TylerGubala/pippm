import argparse, subprocess

parser = argparse.ArgumentParser()

parser.add_argument("name", help="The package that you want to create")

args=parser.parse_args()


print("Are you sure you want to create this package? ({0})".format(args.name))
if input("Y for yes, N for no.") is "Y":
    print("Creating package... {0}".format(args.name))
else:
    print("User canceled package creation. Package {0} was not created.".format(args.name))
#subprocess.call("py -m venv {0}".format())