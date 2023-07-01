# (1)
lis = [1, 6, 3, 2, 4]
def total_list(self):
    total = 0
    if not len(self) == 0:
        for i in self:
            total += i
    return total
print(total_list(lis))

# (2)
st = "apPlegrapeAPPLEbreadApplefapple"
st2 = "apple"
def how_many(string, count):
    total_count = 0
    start = 0
    len_count = len(count)
    for i in range(len(string)):
        if count.lower() in string[start:len_count].lower():
            total_count += 1
        len_count += 1
        start += 1
    return total_count

print(how_many(st, st2))

# (3)
dic = {"hi": "good", "soudane": "soudayo"}
def opposite(self):
    new_dic = {}
    for key,value in self.items():
        new_dic[value] = key
        
    return new_dic

print(opposite(dic))

# (4)
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 9, 1]
def merge(first, second):
    new_list = []
    smaller = len(first)

    if len(first) > len(second):
        smaller = len(second)

    for i in range(smaller):
        new_list.append(first[i])
        new_list.append(second[i])
        
    return new_list

print(merge(list1, list2))
