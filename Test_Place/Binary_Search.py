import math

_list = [5, 10 ,12 ,19, 66, 88, 99]

def binary_search(_list,target):
    l = 0
    r = len(_list) #-1
    while l<r:
        m = math.floor( l+(r-l)/2  )
        if target > _list[m]:
            l = m +1
        elif target < _list[m]:
            r = m
        else:
            return m
    #if l == r:
    #    if target == _list[l]:
    #        return l

    return 'Not Found'


def binary_search_Text(_list, target):
    l = 0
    r = len(_list)-1
    while l < r:
        m = math.floor((l+r)/2)
        if target > _list[m]:
            l = m +1
        else:
            r = m
    if target == _list[l]:
        return l
    else:
        return 'Not Found'


for target in _list:
    print(' target =' + str(target) +'return index = ', binary_search_Text(_list,target) )


g = [-1 , 102]
for target in g:
    print(' target =' + str(target) +'return index = ', binary_search_Text(_list,target) )



