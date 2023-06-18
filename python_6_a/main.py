def total_calculate(self, menu):
    total = 0
    for i in self:
        total += menu[i]
    print(total)
    
# (1)
buy_list = ["りんご", "イチゴ", "パイナップル"]
fruits = {"りんご": 100, "バナナ": 80, "イチゴ": 200, "キウイ": 150, "メロン": 500, "パイナップル": 400}
total_calculate(buy_list, fruits)

# (2)
order_list = ["マルゲリータ", "マリナーラ", "クワトロフォルマッジ"]
pizza = {"マルゲリータ": 1000, "マリナーラ": 1200, "カプリチョーザ": 1400, "クワトロフォルマッジ": 1600}
total_calculate(order_list, pizza)

# (3)
shopping_list = ["りんご", "バナナ", "チーズ", "ヨーグルト"]
quantity = {"りんご": 5, "バナナ": 3, "チーズ": 2, "ヨーグルト": 1}
total_calculate(shopping_list, quantity)

# (4)
grades = [   
 {"name": "Alice", "math": 80, "english": 75, "science": 90},   
 {"name": "Bob", "math": 90, "english": 85, "science": 95},   
 {"name": "Charlie", "math": 70, "english": 65, "science": 80},   
 {"name": "David", "math": 60, "english": 55, "science": 70}
]

# (4)-(1)
def average(self, subject):
    count = 0
    for i in self:
        count += i[subject]
    length = len(self)
    average = count / length
    print(subject + "の全体の平均点は" + str(average) + "点です")
    
average(grades, "math")
average(grades, "english")
average(grades, "science")

# (4)-(2)
import math 
def data(self, name, num):
    total2 = 0
    student_list = list(self[num].values())
    del student_list[0]
    for i in student_list:
        total2 += i
    print(name + "のテストの平均点数は" + str(math.floor(total2 / len(student_list))) + "点です")

data(grades, "Alice", 0)
data(grades, "Bob", 1)
data(grades, "Charlie", 2)
data(grades, "David", 3)

# (4)-(3)
def average(self, subject1, subject2, subject3):
    count1 = 0
    for i in self:
        count1 += i[subject1]
    count2 = 0
    for i in self:
        count2 += i[subject2]
    count3 = 0
    for i in self:
        count3 += i[subject3]
    subject_length = 3
    people_length = 4
    average1 = count1 / people_length
    average2 = count2 / people_length
    average3 = count3 / people_length
    total_average = (average1 + average2 + average3) / subject_length
    print("全科目の平均点は" + str(total_average) + "点です")

average(grades, "math", "english", "science")

# (5)
members = [   
    {"name": "Alice", "age": 20, "gender": "female", "sports": ["basketball", "tennis"]},
    {"name": "Bob", "age": 25, "gender": "male", "sports": ["baseball", "soccer", "volleyball"]},
    {"name": "Charlie", "age": 30, "gender": "male", "sports": ["tennis", "golf"]},
    {"name": "David", "age": 35, "gender": "male", "sports": ["swimming"]}
]

# (5)-(1)
basketball_member = []
for i in members:

    if "basketball" in i["sports"]:
        basketball_member.append(i["name"])
print(basketball_member)

# (5)-(2)
male_list = []
for i in members:
    if i["gender"] == "male":
        male_list.append(i["name"])
print(male_list)

# (5)-(3)
over_30 = []
for i in members:
    if i["age"] >= 30:
        over_30.append(i["name"])
print(over_30)

# (5)-(4)
golf_female = False
for i in members:
    if i["gender"] == "female" and "golf" in i["sports"]:
        golf_female = True
print(golf_female)
