# Global modules
import re
# Local modules
from config import sites_dict

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def handle_url(url):
    for site, regex in sites_dict.iteritems():
        if re.match(regex, url):
            handler = import_from('sites.%s.%s' % (site, site), 'handle_link')
            print handler(url)
            return
