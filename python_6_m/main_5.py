# [問題5: スポーツクラブ]
# あなたは、スポーツクラブのマネージャーです。クラブには、以下のようなメンバーリストがあります。
#
# members = [
#  {"name": "Alice", "age": 20, "gender": "female",
#      "sports": ["basketball", "tennis"]},
#  {"name": "Bob", "age": 25, "gender": "male",
#   "sports": ["baseball", "soccer", "volleyball"]},
#  {"name": "Charlie", "age": 30, "gender": "male",
#   "sports": ["tennis", "golf"]},
#  {"name": "David", "age": 35, "gender": "male", "sports": ["swimming"]}
# ]
#
# 上記のメンバーリストでは、各メンバーの名前(name)、年齢(age)、性別(gender)、スポーツ(sports)が記録されています。あなたは、以下の機能を実装することになりました。
#
# 条件1：バスケットボールをする人のリストを作成する。
# 条件2：男性のリストを作成する。
# 条件3：年齢が30以上の人のリストを作成する。
# 条件4：ゴルフをする女性がいるかどうかを確認する。
# 以上の機能を実現するために、Pythonで必要な処理を行ってください。
print("[問題5: スポーツクラブ]")

members = [
 {"name": "Alice", "age": 20, "gender": "female",
     "sports": ["basketball", "tennis"]},
 {"name": "Bob", "age": 25, "gender": "male",
  "sports": ["baseball", "soccer", "volleyball"]},
 {"name": "Charlie", "age": 30, "gender": "male",
  "sports": ["tennis", "golf"]},
 {"name": "David", "age": 35, "gender": "male", "sports": ["swimming"]}
]

print("条件1")
list1_members = [member.get("name") for member in members]
print(list1_members)

print("条件2")
list2_members = []
for member in members:
    if member.get("gender") == "male":
        list2_members.append(member.get("name"))
print(list2_members)

print("条件3")
list3_members = []
for member in members:
    if member.get("age") >= 30:
        list3_members.append(member.get("name"))
print(list3_members)

print("条件4")
is_exist = False
for member in members:
    if member.get("gender") == "famale" and "golf" in member.get("sports"):
        is_exist = True
        break
print("ゴルフをする女性は" + ("います" if is_exist else "いません"))
