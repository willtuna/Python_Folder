#! /usr/bin/env python3

def item_in_key_order(d):
    return ( (key, d[key]) for key in sorted(d) )


movement = dict(a='left',s='backward',d='right',w='forward')

for r in item_in_key_order(movement):
    print(r)
