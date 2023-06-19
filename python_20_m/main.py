# 【問題1：リストの要素】
# リストの要素を合計する関数を作成してください。
# 以下の要件を満たす関数を作成してください。

# ・リストを受け取り、そのリストの要素をすべて加算し、合計値を返します。
# 空のリストを受け取った場合は、0を返します。
print("【問題1：リストの要素】")

def list_max(arg:list) -> int:
    return sum(arg)

print(list_max([]))
print(list_max([1,2,3,5,7,10]))

# 【問題2：文字列】
# 文字列の中に特定の文字列がいくつ含まれるかを数える関数を作成してください。
# 以下の要件を満たす関数を作成してください。

# ・2つの引数を受け取り、1つ目の引数は文字列、2つ目の引数はカウントする文字列です。
# ・1つ目の引数の中に、2つ目の引数で指定された文字列が何回現れるかをカウントし、その回数を返します。
# ・大文字と小文字を区別しないでカウントします。
print("【問題2：文字列】")

def list_count(string:str,arg:list):
    count = 0
    for i in arg:
        if string.lower() == str(i).lower():
            count += 1
    return count

print(list_count("count",["count" for i in range(5)] + [1,32,5]))

# 【問題3：辞書】
# 辞書のキーと値を入れ替える関数を作成してください。
# 以下の要件を満たす関数を作成してください。

# ・辞書を受け取り、その辞書のキーと値を入れ替えた新しい辞書を返します。
print("【問題3：辞書】")

def dict_reverse(arg:dict):
    return dict(zip(arg.values(),arg.keys()))

print(dict_reverse({1:10,2:20,3:30,4:40}))

# 【問題4：マージ】
# 2つのリストの要素を交互にマージする関数を作成してください。
# 以下の要件を満たす関数を作成してください。

# ・2つの引数を受け取り、1つ目の引数と2つ目の引数の要素を交互にマージした新しいリストを返します。
# ・2つのリストの要素数が異なる場合は、要素数が少ない方に合わせてマージされます。
print("【問題4：マージ】")

def list_merge(first:list,secound:list):
    merge = []
    while(bool(first) or bool(secound)):
        if bool(first):
            merge.append(first.pop(0))
        if bool(secound):
            merge.append(secound.pop(0))
    return merge

print(list_merge([1,2,3,4,5,6],["a","b","c","d","e","f","g","h"]))
