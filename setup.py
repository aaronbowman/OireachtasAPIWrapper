"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""


import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="OireachtasAPI_Wrapper",
    version="1.0.0",
    description="A wrapper for the house of Oirechtas API",
    author="Aaron Bowman",
    author_email="aaron.bowman@leargaseire.com",
    packages=find_packages(where="src"),
    install_requires=['vcrpy',
                      'requests']
)