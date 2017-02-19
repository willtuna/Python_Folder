#! /usr/bin/env python3
import random

default = 5

while True:
    try:
        line=input("Enter a number between 1 to 10 inclusive: ")
        if line:
            iteration = int(line)
            if 1<= iteration <= 10:
                break
            else:
                continue
        else:
            iteration  = default
    except ValueError as err:
        print(err)
        continue


i = 0

while i < iteration:
    articles = ('the','a','etc')
    subjects = ('cat','dog','man','woman')
    verbs = ('sang','ran','jumped')
    adverbs = ('loudly','quietly','well','badly')
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    select = random.randint(0,1)
    if (select == 1):
        print(article,subject,verb)
    else:
        print(article,subject,verb,adverb)
    i +=1




