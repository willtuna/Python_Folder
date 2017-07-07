#! /usr/bin/env python3

import random

list1 = ["one", "two", "three", "four"]

for i in range(3):
    print(random.choice(list1))

print(list1)
random.shuffle(list1)
print(list1)
