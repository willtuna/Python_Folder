#! /usr/bin/env python3
list_num = []
def swap(list_num, a,b):
    temp = list_num[a]
    list_num[a] = list_num[b]
    list_num[b] = temp
    return list_num


def partition(list_num,start,last):
    pivot = list_num[last]
    smaller_front  = start
    next_ = start
    while next_ != last:
        if list_num[next_] < pivot:
            swap(list_num,smaller_front,next_)
            smaller_front +=1
        next_+=1
    


    swap(list_num,smaller_front,last)
    return smaller_front

def qsort(list_num,start,end):
    if (start < end):
        q = partition(list_num,start,end)
        qsort(list_num,start,q-1)
        qsort(list_num,q+1,end)
    
    return list_num








while True:
    line = input("enter a number or Enter to finish: ")
    if( line):
        try:
            number = int(line)
            list_num.append(number)
        except ValueError as err:
            print(err)
    else:
        break

if (list_num):
    sum_ = 0
    for a in list_num:
        sum_ += a
    #list_num.sort()
    qsort(list_num,0,len(list_num)-1)
    print(list_num)
    count = len(list_num)
    if ( (count/2 - count//2) == 0):
        medium = (list_num[int(count/2)] + list_num[int(count/2) - 1] ) / 2
    else:
        medium = list_num[int(count//2)]

    print("count =", count,"sum =", sum_, "lowest = ",list_num[0], "highest =",list_num[count-1], "mean = ",sum_/count ,'medium = ', medium)

