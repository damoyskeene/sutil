from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Search Utility'
LONG_DESCRIPTION = 'A package that creates an abstractive layer for common python tasks.'

# Setting up
setup(
    name="sutil",
    version=VERSION,
    author="Damoy Skeene",
    author_email="<damoydskeene@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'utility', 'string', 'easy', 'beta', 'fast'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)