import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "selenium-crawler",
    version = "0.1.0",
    author = "Cory Walker",
    author_email = "cwalker32@gmail.com",
    description = ("Sometimes sites make crawling hard. Selenium-crawler uses "
                   "Selenium automation to fix that."),
    license = "LICENSE.txt",
    keywords = "selenium crawling crawl automate ads landing",
    url = "https://github.com/cmwslw/selenium-crawler",
    packages=['seleniumcrawler',],
    long_description=read('README.md'),
    install_requires=[
        "selenium == 2.32.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
