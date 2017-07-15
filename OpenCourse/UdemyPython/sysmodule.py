import sys

inputStatement = sys.stdin.readline()
print(inputStatement)
# This sentence is going to be read by the function we just entered
print("read 10 characters")

inputStatement2 = sys.stdin.readline(10)

print(inputStatement2)


sys.stdout.write("Hello ! how are you")
