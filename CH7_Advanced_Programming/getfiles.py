import os
import sys

def get_files(names):
    return (file for file in names if os.path)

print(get_files(sys.argv[1:]))


