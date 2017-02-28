#! /usr/bin/env python3
import sys

while(1):
    try:
        str1=input()
        ans = eval(str1) %(1e9 + 7)
        print(int(ans))
    except EOFError:
        break        
        
sys.exit()
