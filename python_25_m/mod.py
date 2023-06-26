def convert(cards:list) -> int:
    total = 0
    ones = 0
    for card in cards:
        match card:
            case 'K' | 'Q' | 'J':
                total += 10
                continue
        num = int(card)
        if num == 1:
            ones += 1
        else:
            total += num
    for _ in range(ones):
        ones -=1
        if total >= 11:
            total += 1
        elif ones == 0:
            total += 11
        elif (10-ones) >= total:
            total += 11
        else:
            total += 1
    return total

def get_int(string: str) -> int:
    while True:
        try:
            text = input(string)
            value = int(text)
            return value
        except Exception:
            print("整数を入力してください")
