from mod import get_int


integer = get_int()
for i in range(1, integer + 1):
    string = ""
    if i % 15 == 0:
        string = "Fizz Buzz"
    elif i % 3 == 0:
        string = "Fizz"
    elif i % 5 == 0:
        string = "Buzz"
    else:
        string = i
    print(string)
