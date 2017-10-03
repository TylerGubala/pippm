# pippm
A python package manager for pip

The goal of this repository is to make it easy for the average person to install package dependencies, create tests, with colorful printing and a rich output which can be viewed by anyone in a terminal

#Getting Started

To install pippm (pip package manager) simply type 

```py -m pip install pippm```

This will automagically install the latest version of pippm for your version of python

#Usage 

pippm is inspired by npm (Node package manager), and therefore acts similarly. To start a new code project, simply type 

```py pippm init```

It will initialize a package for you and walk you through the process.

Overview of pippm functions:

 - init : initialize a package at the location (if specified) with a folder system and bare minimum files
 - test : run a test which has been named in the 'tests' portion of the package.json
 - build: create a build file (executable) out of the package (platform dependent)
 - remove: remove the package at location (if specified) otherwise look in the CWD and delete the directory recursively IF the directory contains a package.json at the root
 - deploy: send the updated package to pip (--language=python) or npm (--language=javascript)
 - environment: add an environment to the package with the matching platform (check for bitness, operating system, etc)

Hopefully this is helpful to some other programmers out there.