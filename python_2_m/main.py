import random
# 1) 自分の名前を出力してください。
print("(1)")
print("moriyoshi")
# 2) 入力された名前から「こんにちは。◯◯さん」という文字列を出力してください。
print("(2)")
name = input("名前を入力してください ")
print("こんにちは。" + name + "さん")
# 3) ランダムに取り出した2つの数を掛け算してその答えを出力してください。
print("(3)")
print(random.randint(1, 10) * random.randint(1, 10))
# 4) 入力された2つの数値を足してその答えを出力してください。
first = int(input("数字を入力してください "))
second = int(input("数字を入力してください "))
print(first + second)
