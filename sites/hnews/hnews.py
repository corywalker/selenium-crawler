from selenium import webdriver

def handle_link(link):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(link)

    driver.find_element_by_xpath("//td[@class='title']/a").click()

    return {
        'url': driver.current_url,
        'source': driver.page_source
    }
