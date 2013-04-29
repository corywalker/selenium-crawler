# Global modules
import os
# Local modules
from seleniumcrawler.config import sites_dict

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SITES_DIR = os.path.join(THIS_DIR, 'sites')
def locate_sites():
    location_list = []
    for site, regex in sites_dict.items():
        this_site_dir = os.path.join(SITES_DIR, site)
        # This is only the EXPECTED script name.
        # All scripts should follow this convention.
        script_name = site + '_raw.py'
        script_path = os.path.join(this_site_dir, script_name)
        config_path = os.path.join(this_site_dir, 'config.py')
        location_dict = {
            'name': site,
            'script_path': script_path,
            'config_path': config_path,
            'site_dir': this_site_dir
        }
        location_list.append(location_dict)

    return location_list
