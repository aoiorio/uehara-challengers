while True:
    integer = input("Tell me the first number: ")
    if not integer.isdigit():
        print("Please make it an integer")
        continue
    else:
        integer = int(integer)
        break

while True:
    integer2 = input("Tell me the second number: ")
    if not integer2.isdigit():
        print("Please make it an integer")
        continue
    else:
        integer2 = int(integer2)
        break

print("Your total number is " + str(integer + integer2))