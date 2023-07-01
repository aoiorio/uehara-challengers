# (1)
breads = {"french bread": 10, "roll bread": 10, "croissant": 10, "pain au chocolate": 10}

for i,val in breads.items():
    val -= 1
    print(str(i) + "の在庫は残り" + str(val) + "個です")

# (2)
number_list = [1, 3, 5, 7, 9]
total = 0
for i in number_list:
    total += i
print(total)

# (3)
menu = ["coffee", "tea", "hamburger", "soup", "sandwich"]
while menu:
    for i in menu:
        print(i)
    break

# (4)
for i in range(1, 10):
    print(str(i) + "の段")
    for j in range(1, 10):
        print(i * j)