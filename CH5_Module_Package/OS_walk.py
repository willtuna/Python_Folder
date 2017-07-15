import os


# os.walk only accept absolute path for traversal
for dirPath, dirNames, fileNames in os.walk("/home/willvegapunk/Programming/Python3/"):
    print(dirPath)
    for f in fileNames:
        print(os.path.join(dirPath, f))


print('Absolute Path', os.path.abspath('.'))
print('os.path.split:\n',os.path.split('./Heap/heap_.py'))
