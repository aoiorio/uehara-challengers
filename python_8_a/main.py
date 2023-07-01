# (1)
food = input("ピザ、ハンバーガー、サラダの中から選んでください: ")
calorie = input("選んだ食べ物のカロリーを入力してください: ")

if food == "ピザ" and int(calorie) < 500:
    print("ピザを注文しました")
elif food == "ピザ" and int(calorie) > 500:
    print("高カロリーなピザです。気をつけてください")
elif food == "ハンバーガー" and 300 < int(calorie) < 500:
    print("ハンバーガーを注文しました")
elif food == "ハンバーガー" and int(calorie) < 300:
    print("ハンバーガーではお腹がいっぱいになりません。何かもう一つ注文しましょう")
elif food == "サラダ" and 200 < int(calorie) < 300:
    print("サラダを注文しました。健康的な選択です。")
elif food == "サラダ" and int(calorie) < 200:
    print("サラダは低カロリーです。もう一つ何か注文してもいいんじゃないですか？")

# (2)
weather = input("今日の天気予報を入力してください: ")

if weather == "晴れ" :
    print("日焼け止めを持っていきましょう")
elif weather == "曇り":
    print("薄手のジャケットがあると便利です")
else:
    print("傘を持っていきましょう")

# (3)
term = input("提出期限を入力してください: ")

if term == "今日中":
    print("急いで提出しましょう")
elif term == "明日まで":
    print("明日の朝までに提出しましょう")
elif term == "2日後まで" or term == "二日後まで":
    print("余裕を持って提出しましょう")