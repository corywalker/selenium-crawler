# Global modules
import os
# Third party modules
import pystache
# Local modules
from seleniumcrawler.filesystem import locate_sites

template = '''from selenium import webdriver
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

{{{code}}}
    results = {
        'url': driver.current_url,
        'source': driver.page_source
    }
    driver.quit()

    return results
'''

def parse_raw_script(name, directory, path):
    f = open(path)

    codelines = []
    at_main_code = False
    for line in f:
        if at_main_code:
            codelines.append(line[4:])
        if line.startswith('    def test_'):
            at_main_code = True
        elif line.startswith('    def') and at_main_code:
            codelines = codelines[1:-2]
            at_main_code = False
            break

    fout = open(os.path.join(directory, name + '.py'), 'w')
    code = ''.join(codelines)
    data = {'code': code}
    rendered = pystache.render(template, data)
    fout.write(rendered)

for site in locate_sites():
    parse_raw_script(site['name'], site['site_dir'], site['script_path'])
    print "Parsed %s." % site['script_path']
