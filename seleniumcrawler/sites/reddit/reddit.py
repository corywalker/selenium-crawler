from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def get_profile():
    # get the Firefox profile object
    firefoxProfile = FirefoxProfile()
    # Disable CSS
    firefoxProfile.set_preference('permissions.default.stylesheet', 2)
    # Disable images
    firefoxProfile.set_preference('permissions.default.image', 2)
    # Disable Flash
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',
                                    'false')

    return firefoxProfile

def handle_link(link):
    profile = get_profile()

    # Set the modified profile while creating the browser object
    driver = webdriver.Firefox(profile)
    driver.implicitly_wait(30)
    driver.get(link)

    driver.find_element_by_xpath("//p[@class='title']/a").click()

    results = {
        'url': driver.current_url,
        'source': driver.page_source
    }
    driver.quit()

    return results
