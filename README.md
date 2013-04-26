selenium-crawler
================

Have you ever needed to crawl a list of urls that may or may not directly contain the content you so desperately crave? The web is full of links that do not behave for a number of reasons, and here is a list of just some of them:

1. The page is actually a landing page that links to the page you want
  * Hacker News
  * Hack-a-day
  * Reddit
2. The page content is only made available after closing an ad:
  * Forbes
3. The content is behind some sort of login or paywall:
  * Boston Globe
4. One must click through some sort of pagination to find the content:
  * Web forums

You might be asking, why use Selenium when you can use a combination of PhantomJS and BeautifulSoup to extract the needed data? This is a great way to accomplish some of the listed tasks above, but it has a number of limitations:

* Business teams would sometimes rather work with a visual tool rather than writing lines of code.
* Selenium has most of the code that would be needed already built in.

Depending on Selenium DOES NOT mean that your crawling servers will need to also run a GUI. Selenium can run in a headless environment. Look this up for more information.

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

