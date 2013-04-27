# Global modules
import os

SITES_DIR = './sites'
def locate_sites():
    sites = os.listdir(SITES_DIR)

    location_list = []
    for site in sites:
        # Filter out hidden directories
        if site.startswith('.'):
            continue
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
