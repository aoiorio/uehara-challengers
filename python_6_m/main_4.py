# 【問題4：先生気分】
# あなたは、ある学校の成績処理をすることになりました。学校には、以下のような成績表があります。
#
# grades = [
#  {"name": "Alice", "math": 80, "english": 75, "science": 90},
#  {"name": "Bob", "math": 90, "english": 85, "science": 95},
#  {"name": "Charlie", "math": 70, "english": 65, "science": 80},
#  {"name": "David", "math": 60, "english": 55, "science": 70}
# ]
#
# 上記の成績表では、各生徒の名前(name)と、数学(math)、英語(english)、理科(science)の点数が記録されています。あなたは、以下の機能を実装することになりました。
#
# 条件1：各科目の平均点を計算する。
# 条件2：各生徒の平均点を計算する。
# 条件3：全科目の平均点を計算する。
# 以上の機能を実現するために、Pythonで必要な処理を行ってください。
print("【問題4：先生気分】 ")

grades = [
 {"name": "Alice", "math": 80, "english": 75, "science": 90},
 {"name": "Bob", "math": 90, "english": 85, "science": 95},
 {"name": "Charlie", "math": 70, "english": 65, "science": 80},
 {"name": "David", "math": 60, "english": 55, "science": 70}
]

print("条件1")
gets = ["math", "english", "science"]
length = len(grades)
for g in gets:
    all = 0
    for v in grades:
        all += v.get(g)
    print(g + "の平均点は " + str(all/length) + " 点です")

print("条件2")
subjects = len(gets)
for g in grades:
    name = ""
    points = 0
    for key, value in g.items():
        if key == "name":
            name = value
            continue
        points += value
    print(name + " の平均点は" + str(int(points/subjects)) + " です")

print("条件3")
points = 0
num = 0
for g in grades:
    for key, value in g.items():
        if key == "name":
            continue
        num += 1
        points += value
print("全科目の平均点は " + str(points/num) + " です")
