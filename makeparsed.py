import os

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
    return {
        'url': driver.current_url,
        'source': driver.page_source
    }
''')

SITES_DIR = './sites'
sites = os.listdir(SITES_DIR)

for site in sites:
    # Filter out hidden directories
    if site.startswith('.'):
        continue
    this_site_dir = os.path.join(SITES_DIR, site)
    # This is only the EXPECTED script name.
    # All scripts should follow this convention.
    script_name = site + '_raw.py'
    script_path = os.path.join(this_site_dir, script_name)
    parse_raw_script(site, this_site_dir, script_path)
    print "Parsed %s." % script_path
