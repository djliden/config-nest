import os
from setuptools import setup
from setuptools import find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="confignest",
    version="0.0.1",
    author="Daniel Liden",
    author_email="dliden@pm.me",
    description=("A small configuration and logging system for machine"
                 "learning projects"),
    license="MIT",
    keywords="example documentation tutorial",
    url="https://github.com/djliden/config-nest",
    long_description=read('README.md'),
    packages=find_packages(include=['confignest', 'confignest.*', 'tests']),
    install_requires=['pyyaml'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
