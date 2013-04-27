from selenium import webdriver

def handle_link(link):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(link)

    driver.find_element_by_xpath("//p[@class='title']/a").click()

    results = {
        'url': driver.current_url,
        'source': driver.page_source
    }
    driver.quit()

    return results
