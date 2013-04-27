# Global modules
import os
# Local modules
from filesystem import locate_sites

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
    fout.write(
    '''from selenium import webdriver

def handle_link(link):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(link)

''')
    code = ''.join(codelines)
    fout.write(code)
    fout.write('''
    results = {
        'url': driver.current_url,
        'source': driver.page_source
    }
    driver.quit()

    return results
''')

for site in locate_sites():
    parse_raw_script(site['name'], site['site_dir'], site['script_path'])
    print "Parsed %s." % site['script_path']
