from setuptools import setup, find_packages

setup(
    name='OireachtasAPIWrapper',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/aaronbowman/OireachtasAPIWrapper',
    license='MIT',
    author='Aaron Bowman',
    author_email='aaronrbowman12@gmail.com',
<<<<<<< HEAD
    description='A Python wrapper for the Oireachtas (Irish Parliament) Open Data API',
    install_requires=[
        'requests>=2.32',
    ]
=======
    description='Python client for the Irish Oireachtas public API',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.31',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
>>>>>>> df46be9a75c229a86acd3777c1f54d19c556bc78
)
