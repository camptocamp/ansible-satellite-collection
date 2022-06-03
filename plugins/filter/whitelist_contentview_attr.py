def whitelist_contentview_attr(a):
    new_hash = {}
    if 'product' in a:
        new_hash['product'] = a['product']
    if 'name' in a:
        new_hash['name'] = a['name']
    return new_hash

class FilterModule(object):

    def filters(self):
        return {
                'whitelist_contentview_attr': whitelist_contentview_attr,
        }

