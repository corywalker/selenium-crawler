selenium-crawler 0.1.0
======================

Have you ever needed to crawl a list of urls that may or may not directly
contain the content you so desperately crave? The web is full of links that do
not behave for a number of reasons, and here is a list of just some of them:

1. The page is actually a landing page that links to the page you want:
  * Hacker News
  * Hack-a-day
  * Reddit
2. The page content is only made available after closing an ad:
  * Forbes
3. The content is behind some sort of login or paywall:
  * Boston Globe
4. One must click through some sort of pagination to find the content:
  * Web forums

You might be asking, why use Selenium when you can use a combination of
PhantomJS and BeautifulSoup to extract the needed data? This is a great way to
accomplish some of the listed tasks above, but it has a number of limitations:

* Business teams would sometimes rather work with a visual tool rather than
  writing lines of code.
* Selenium has most of the code that would be needed already built in.

**Depending on Selenium DOES NOT mean that your crawling servers will need to
also run a GUI. Selenium can run in a headless environment. See below for more
information.**

Quickstart
==========

```bash
pip install -e git+https://github.com/cmwslw/selenium-crawler.git#egg=selenium-crawler
```

```python
from seleniumcrawler import handle_url
print handle_url('https://news.ycombinator.com/item?id=5626377')
```

This will open up a browser window, 'click' on the main link, and load the
article. It will print the following:

```python
{
    'url': 'http://googleblog.blogspot.com/2013/04/google-now-on-your-iphone-and-ipad-with.html',
    'source': {{HTMLSOURCE}},
    'handler': 'hnews'
}
```

Where `{{HTMLSOURCE}}` is the actual HTML of the article.

Creating test cases
===================

Create test cases as you normally would in Selenium, but be sure to take the
following things into account:

### Never make a test case article-specific
By default, when one records Selenium test cases, the very first instruction
will be for the browser to load up a specific URL. This url will be the current
article that you are viewing. Since you will be designing scripts that should
work for ANY given article on the site. Make sure you always remove this line. I
might make selenium-crawler take care of this step in the future. That is TBD.

### Make your locators as robust as possible
On the one hand, make the locators specific enough to be confident that the
will only match exactly what needs to be matched. On the other hand, make sure
that your locator will continue to match even in the case of a website theme
change or even redesign. It is impossible to account for every possible change
in site structure, but you get the idea. By default, Selenium tends to create
very specific locators while recording. Make sure to fix these up a bit.

### Save test cases in a standard way
While it really doesn't matter where saved test case files even go, for
reference and debugging purposes it is useful to save them in a standard
location. For the time being, I have established the form
`sites/{name}/{name}.tc`. Hopefully this will prove to be a decent convention.

Exporting test cases
====================

Selenium-crawler takes in exported selenium Python scripts as inputs. Follow
these instructions to obtain the exported scripts. Be sure to use the WebDriver
backend.

![ScreenShot](https://raw.github.com/cmwslw/selenium-crawler/master/docs/exporting_tc.png)

Next we need to save the script in a place where selenium-crawler can find it.
Find the sites directory. Next, create a directory for the site. Choose a
useful, concise name. Save the actual exported script in the format of
`{name}_raw.py`:

![ScreenShot](https://raw.github.com/cmwslw/selenium-crawler/master/docs/saving_tc.png)

Parsing selenium cases
======================

The test cases that Selenium exports are not even valid Python code. Here is an
example:

```python
self.accept_next_alert = true
```

Once you fix the syntax errors, they are useful for writing test suites, but not
for writing crawlers. Running `python makeparsed.py` takes all these Selenium
test cases and converts them to Python code usable for crawling. Here is an
example that clicks through an annoying Javascript ad on Forbes pages:

```python
from selenium import webdriver

def handle_link(link):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(link)

    driver.find_element_by_xpath("//div[@class='header']/div[@class='continue']/a").click()

    results = {
        'url': driver.current_url,
        'source': driver.page_source
    }
    driver.quit()

    return results
```

So go ahead. Run `python makeparsed.py`. You should see output similar to the
following:

```
Parsed ./sites/forbes/forbes_raw.py.
Parsed ./sites/hnews/hnews_raw.py.
Parsed ./sites/reddit/reddit_raw.py.
```

Don't worry if the paths are different for your installation. Keep in mind that
`makeparsed.py` only has to be run when site scripts have either been changed
or added.

Headless configuration
======================

Running headless means that no actual GUI will be running on a monitor during
use. Put simply, it means that no browser window will pop up when handling a
URL. One way to run headless is through the use of xvfb, a tool used to set up
virtual framebuffers. Run this before using selenium-crawler:

```bash
sh -e /etc/init.d/xvfb start
export DISPLAY=:99.0
```

This is the method that CI systems like Travis-CI and CircleCI recommend. There
are other methods of running Selenium in a headless environment. Do a quick
Google search for more information.

Contributing
============

Contributing is easy. If you write any new site handling scripts, just be sure
to follow the guide above and write a quick test for it in `test_all.py`. Just
send in a pull request and I'll get a `CONTRIBUTORS.txt` file going.

