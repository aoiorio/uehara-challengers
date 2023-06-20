list1 = [1, 3, 2, 5, 5, 7, 6, 8, 9, 10]


def odd_and_even(self):
    odd = []
    even = []
    for i in self:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(sorted(even))
    print(sorted(odd, reverse=True))

odd_and_even(list1)