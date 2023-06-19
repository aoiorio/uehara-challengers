# 【問題1：リスト】
# リストを引数として受け取り、偶数と奇数のリストに分けて返す関数を作成してください。ただし、偶数リストは小さい順に、奇数リストは大きい順に並べ替えることとします。
print("【問題1：リスト】")

def diff_list(list: list) -> list:
    list_even = []
    list_odd = []
    for i in list:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)
    list_even.sort()
    list_odd.sort(reverse=True)
    return [list_even,list_odd]

print(diff_list([1,43,654,323,432,]))

# 【問題2：リスト②】
# リストを引数として受け取り、重複する要素を削除し、リスト内の要素を数値順に並べ替えた上で、最初の3つの要素を返す関数を作成してください。
print("【問題2：リスト②】")

def third_list(array: list) -> list:
    copy = list(set(array))
    copy.sort()
    return copy[0:3]

print(third_list([1,1,5435,5435,432,5,6,7,7]))

# 【問題3：文字列】
# 文字列を引数として受け取り、文字列中の単語をすべて逆順にし、単語の順番を逆転させた新しい文字列を返す関数を作成してください。ただし、単語は空白で区切られているものとします。
print("【問題3：文字列】")

def reverse_word(string:str) -> str:
    split = string.split()
    split.reverse()
    return " ".join(split)

print(reverse_word("I am programmer"))

# 【問題4：リスト3】
# 2つのリストを引数として受け取り、それらのリストの中で重複する要素を抽出し、新しいリストとして返す関数を作成してください。ただし、重複する要素がない場合は空のリストを返すこととします。
print("【問題4：リスト3】")

def duplication_list(first:list,second:list) ->list:
    return list(set(first).intersection(set(second)))

print(duplication_list([1,2,3,4,5,6],[1,2,3,6]))

# 【問題5：辞書】
# 辞書を引数として受け取り、辞書の値が数値である場合に、その値を2倍にした辞書を返す関数を作成してください。ただし、元の辞書は変更しないこととします。
print("【問題5：辞書】")

def twice_dict(dictionary:dict) -> dict:
    return dict(zip(dictionary.keys(),[i * 2 if isinstance(i,float) else i for i in dictionary.values()]))

print(twice_dict({1:10,2:"hello",10:100}))
