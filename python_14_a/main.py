# (1)
list1 = [1, 3, 2, 5, 5, 7, 6, 8, 9, 1]

def odd_and_even(self):
    odd = []
    even = []
    for i in self:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return str(sorted(even)) + ", " + str(sorted(odd, reverse=True))

print(odd_and_even(list1))

# (2)
def change_list(self):
    new_list = sorted(set(self))
    return str(new_list[0]) + ", "+ str(new_list[1]) + ", " + str(new_list[2])

print(change_list(list1))

string_list = "s t r i n g t a t i d a y o"
# (3)
def string(self):
    self_reversed = ''.join(list(reversed(self)))
    new_self_reversed = self_reversed.replace(' ', '') # replaceで空白のところを何もない状態にする
    return new_self_reversed

print(string(string_list))

# (4)
list2 = [1, 2, 3, 5, 7, 8]
list3 = [1, 2, 6, 11, 9, 10]
new_list1 = []

def same_string(self, second):
    for i in self:
        for j in second:
            if j == i:
                new_list1.append(j)
    return new_list1

print(same_string(list2, list3))

# (5)
dic = {"apple": 1, "grape": "one", "orange": 9}
new_dic = {}
def search_num(self):
    for k, v in self.items():
        if isinstance(v, int):
            new_dic[k] = v * 2
    return new_dic
print(search_num(dic))

