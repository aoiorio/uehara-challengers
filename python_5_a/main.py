list1 = [4, 7, 1]

def find_max(self):
    maxsan = None # maxsan をここで代入しないとmaxsanが定義されていないことになる（グローバルで定義していた）
    if not len(self) < 1:
        for i in self:
            for j in self:
                if i > j:
                    maxsan = i
                
    print(maxsan)
    
find_max(list1)