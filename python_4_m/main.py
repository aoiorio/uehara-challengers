from mod import get_int, prime_number

num = get_int()
print(str(num) + "は素数で" + ("す" if prime_number(num) else "はありません") + "。")
