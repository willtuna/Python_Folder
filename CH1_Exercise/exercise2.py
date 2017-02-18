#! /usr/bin/env python3
list_num = []
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
    list_num.sort()
    print(list_num)
    count = len(list_num)
    print("count =", count,"sum =", sum_, "lowest = ",list_num[0], "highest =",list_num[count-1], "mean = ",sum_/count )

