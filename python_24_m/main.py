from mod import get_int
# 合計△L入るお風呂に、毎分□Lの割合で水を入れる。
# 満タンになったら水を止めてもらう、素晴らしく便利なタイマーを作ろう。
# 出力
# 1）お風呂の最大量を入力させる
# 2）毎分の水の量を入力させる
# 3）入水量を毎分置きに表示する
# 4）お風呂が満水になったら3）が止まる

# この順番で出力してみよう。
liter = get_int("お風呂の容量は何Lですか？")
time_water = get_int("毎分何L水がたまりますか？")
water = 0
while True:
    water += time_water
    if liter > water:
        print("現在{}/{}L溜まっています".format(water,liter))
        continue
    print("お風呂が溜まりました！")
    break
