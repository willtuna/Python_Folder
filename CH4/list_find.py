#! /usr/bin/env python3
# This is the test for the while loop with else clause

def list_find(lst,target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
    return index
def list_find_for(lst,target):
    for index,x in enumerate(lst):
        if x == target:
            break
    else:
        index = -1 # notice that index could still be used !!!!

    return index

def list_find_final(lst,target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index


def main():
    try:
        list1 = [1,2,3,4,5,6]
        print('list1 contain',list1,'\nWhich one you would like ?')
        target = input('Enter a number')
        #  Aware !!! the value read from the keyboard is always str type, so you need conversion 
        index = list_find_final(list1,int(target))   if int(input('Using for loop ?(1/0)')) else  list_find(list1,int(target))
        print('This index is', index)
    except ValueError:
        print('Vega Exception!!! ValueError:\n Your input is',target)
    else:
        print('Execute else suit: Everything is fine, no exception occured !!')
    return

main()
