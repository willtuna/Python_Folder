

import sys


def extract_from_tag(tag,line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        end = line.index(closer)
        return line[start:end]
    except ValueError:
        return None



def extract_from_tag2(tag,line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        end = line.find(closer)
        if end!=-1:
            return line[start:end]
    
    
    return None







print(sys.argv[1])
print(sys.argv[2])
print(extract_from_tag(sys.argv[1], sys.argv[2]))
print("2nd Version\n"+extract_from_tag2(sys.argv[1], sys.argv[2]))




