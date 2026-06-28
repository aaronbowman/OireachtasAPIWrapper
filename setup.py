from setuptools import setup, find_packages

setup(
    name='OireachtasAPIWrapper',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/aaronbowman/OireachtasAPIWrapper',
    license='MIT',
    author='Aaron Bowman',
    author_email='aaronrbowman12@gmail.com',
    description='A Python wrapper for the Oireachtas (Irish Parliament) Open Data API',
    install_requires=[
        'requests>=2.32',
    ]
)
