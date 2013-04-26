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

The test cases that Selenium exports are not even valid Python code. Here is an example:

```python
self.accept_next_alert = true
```

Once you fix the syntax errors, they are useful for writing test suites, but not for writing crawlers. Running `python makeparsed.py` takes all these Selenium test cases and converts them to Python code usable for crawling. Here is an example:

```python
from selenium import webdriver

def handle_link(link):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(link)

    driver.find_element_by_xpath("//div[@class='header']/div[@class='continue']/a").click()

    return {
        'url': driver.current_url,
        'source': driver.page_source
    }
```

So go ahead. Run `python makeparsed.py`. You should see output similar to the following:

```
Parsed ./sites/forbes/forbes_raw.py.
Parsed ./sites/hnews/hnews_raw.py.
Parsed ./sites/reddit/reddit_raw.py.
```

What's next?
============
selenium-crawler is still in a very early testing stage. You might not even call it that. I still need to test with a variety of different Selenium test cases to make sure my parsing is robust enough. Before I work on that, however, I plan to write a wrapper that will take a simple link and automatically route it through the right site handler based on the URL.

