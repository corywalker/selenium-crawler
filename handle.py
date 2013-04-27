# Global modules
import re
# Local modules
from config import sites_dict

class HandlerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def handle_url(url):
    for site, regex in sites_dict.iteritems():
        if re.match(regex, url):
            handler = import_from('sites.%s.%s' % (site, site), 'handle_link')
            result = handler(url)
            result['handler'] = site
            return result
    raise HandlerError('Handler for URL not defined')
