#! /urs/bin/env python3
import sys
import heapq

heap = []


heapq.heappush(heap, (5, 'rest'))
heapq.heappush(heap, (2, 'work'))
heapq.heappush(heap, (4, 'study'))

print(heap)


for x in heapq.merge([1,3,5,8],[2,4,11,9]):
    print(x, end='  ')

print('\nEnd of Heap',file=sys.stdout)
    
