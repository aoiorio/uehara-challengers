# 【問題1：パン屋さんの在庫管理】
# あるパン屋さんでは、毎日焼きたてのパンを販売しています。パンの種類は、以下の4つです。
#
# フランスパン
# ロールパン
# クロワッサン
# パン・オ・ショコラ
# パン屋さんでは、各種類のパンを10個ずつ焼いています。以下のようなループ処理を使って、パンの在庫を管理するPythonコードを作成してください。

print("【問題1：パン屋さんの在庫管理】")
bread_list = ["フランスパン", "ロールパン", "クロワッサン", "パン・オ・ショコラ"]
pan_stock = [10, 10, 10, 10]
for i in range(len(bread_list)):
    print(bread_list[i] + ": " + str(pan_stock[i]) + "個")

# 【問題2：数の足し算】
# 以下の数のリストがあります。
# number_list = [1, 3, 5, 7, 9]
# このリストの中の数を一つずつ、すべて足し合わせるPythonコードを作成してください。
print("【問題2：数の足し算】")
number_list = [1, 3, 5, 7, 9]
max = 0
for v in number_list:
    max += v
print(max)

# 【問題3：カフェのメニュー表示】
# あるカフェで働いているあなたは、メニューを表示するプログラムを作成しています。以下のように、
# カフェのメニュー（ドリンクと料理）をリストで用意し、whileループを使ってメニューを表示するプログラムを作成してください。
#
# カフェのメニュー
# 　・コーヒー
# 　・紅茶
# 　・ハンバーガー
# 　・スープ
# 　・サンドイッチ
print("【問題3：カフェのメニュー表示】")
cafe_list = ["コーヒー", "紅茶", "ハンバーガー", "スープ", "サンドイッチ"]
print("カフェのメニュー")
while bool(cafe_list):
    print("・" + cafe_list.pop())

# 【問題4：九九の】
# 九九の表を表示するPythonコードを作成してください。
print("【問題4：九九の】")

# x  1  2  3  4  5  6  7  8  9
# 1  1  2  3  4  5  6  7  8  9
# 2  2  4  6  8  10 12 14 16 18
# 3  3  6  9  12 15 18 21 24 27
# 9  9  18 27 36 45 54 63 72 81


def print_line(list: list):
    line = ""
    for v in list:
        string = str(v)
        while len(string) != 3:
            string += " "
        line += string
    print(line)


vowel = [num for num in range(1, 10)]
print_line(["x"] + vowel)
for v in vowel:
    print_line([v] + [num * v for num in vowel])
