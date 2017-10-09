import json
from setuptools import setup, find_packages

with open("package.json", "r") as packageFile:

    packageJson = json.loads(packageFile.read())

    setup(
        name = packageJson['name'],
        version = packageJson['version'],
        packages = find_packages(),
        install_requires = packageJson['dependancies'],
        package_data = packageJson['package_data'],
        author = packageJson['author'],
        author_email = packageJson['author_email'],
        description = packageJson['description'],
        long_description = packageJson['long_description']
        license = packageJson['license']
        keywords = packageJson['keywords']
        url = packageJson['url']
    )