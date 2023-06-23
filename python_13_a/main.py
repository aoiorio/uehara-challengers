# (1)
height  = int(input("身長を入力してください: "))
height = height * 0.01
# (2)
weight = int(input("体重を入力してください: "))

# (3)
bmi = weight / (height ** 2)

# (4)
if bmi < 18.5:
    print("低体重です。もうちょっと何か食べてもいいんじゃないですかね")
elif 18.5 <= bmi < 25.0:
    print("普通体重です。ちょうどいい感じです")
elif 25.0 <= bmi < 30:
    print("肥満(1度)です。ミネラルが足りていません")
elif 30 <= bmi < 35.0:
    print("肥満(2度)です。マックの食べ過ぎですね")
elif 35.0 <= bmi < 40.0:
    print("肥満(3度)です。アイスクリームを夜中に3kg以上食べるのはやめましょう")
elif 40.0 <= bmi:
    print("肥満(4度)です。3日間絶食をしてみましょう")