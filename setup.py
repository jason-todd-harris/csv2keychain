# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('csv2keychain-onowahoo/__main__.py').read(),
    re.M
).group(1)

setup(
    name="cmdline-csv2keychain-onowahoo",
    packages=["csv2keychain-onowahoo"],
    entry_points={
        "console_scripts": ['csv2keychain-onowahoo = csv2keychain-onowahoo.__main__:main']
    },
    version=version,
    description="Tool for adding exported credentials from Chrome to the macOS keychain.",
    author="Nikita Tarasov",
    author_email="mail@ntarasov.ru",
    url="https://github.com/nntarasov/csv2keychain",
)
