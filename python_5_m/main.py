def find_max(list: list):
    if len(list) == 0:
        return None
    max = list[0]
    for v in list:
        if v > max:
            max = v
    return max


# 例1
lst1 = [3, 5, 1, 8, 2]
print(find_max(lst1))

# 例2
lst2 = [4, 4, 4, 4, 4]
print(find_max(lst2))

# 例3
lst3 = []
print(find_max(lst3))
