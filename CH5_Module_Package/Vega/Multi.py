#! /usr/bin/env python3
'''
>>first()
>>second()

This is the how to use the method in this module

'''


__all__ = ['first','second']



def first():
    print('first in __all__')

def second():
    print('second not in __all__, call me by from  Vega.multi import second')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
