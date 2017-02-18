print("Enter the integer,  Enter or ^D or ^d for end this program")

count = 0
total = 0

while True:
    try:
        line = input("Integer :")
        if line:
            try:
                number = int(line)
            except ValueError as err:
                print(err)
                continue
            count += 1
            total +=  number
    except EOFError:
        break


if count:
    print("count =", count, "total = ", total, "mean = ", total/count)
