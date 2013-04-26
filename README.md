selenium-crawler
================

This project is a work in progress. More documentation will be added once the project stabilizes.

Exporting test cases
====================

selenium-crawler takes in exported selenium Python scripts as inputs. Follow these instructions to obtain the exported scripts. Be sure to use the WebDriver backend.

![ScreenShot](https://raw.github.com/cmwslw/selenium-crawler/master/docs/exporting_tc.png)

Next we need to save the script in a place where selenium-crawler can find it. Find the sites directory. Next, create a directory for the site. Choose a useful, concise name. Save the actual exported script in the format of {name}_raw.py:

![ScreenShot](https://raw.github.com/cmwslw/selenium-crawler/master/docs/saving_tc.png)

Parsing selenium cases
======================

The test cases that Selenium exports are not even valid Python code. Once you fix the syntax errors, they are useful for writing test suites, but not for writing crawlers. Running `python makeparsed.py` takes all these Selenium test cases and converts them to Python code usable for crawling. Here is an example:
