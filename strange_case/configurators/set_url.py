import urllib

from strange_case.configurators import is_index


def set_url(source_file, config):
    if is_index(config):
        config['url'] = ''
    else:
        config['url'] = urllib.quote(config['target_name'])
    return config

set_url.require_after = ['url']