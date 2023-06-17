import random

print("【問題1】")
string = input("文字を入力してください: ")
print(string + " は回文" + ("です" if string == ''.join(
    list(reversed(string)))else "ではないです"))

print("【問題2】")
integer = random.randint(1, 101)
string = ""
if integer >= 80:
    string = "優"
elif integer >= 60:
    string = "良"
else:
    string = "可"
print(string)
