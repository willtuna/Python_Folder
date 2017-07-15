

a = 5
a += 5 # a fisrt be evaluated then added with 5 to create a new integer, which later would be  bound to 'a' object reference
print (a)


#By Default the Python's Division return the float type
print("10/3 is equal to",a/3)


#String and list are the iterating object so bydefault it has operator overloading with +=
name = "Will"
name += "Vegapunk" # string is immutable so its procedure is just like a+=5
print(name)

seeds = ["sesame", "sunflower"]
seeds += ["pumpkin"]# There is a little difference


#seeds += 5 would be error since 5 is not list object
seeds += [5]
print(seeds)


seeds += "Hello"# Hello is the iteration of characters, so list store each character
print(seeds)

