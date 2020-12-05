passes = [x.strip() for x in open('day5/input.txt').readlines()]

def search(ins, lower, higher, min, max):
    for i in ins:
        if i == lower:
            max = max - ((max - min) // 2) - 1
        elif i == higher:
            min = min + ((max - min) // 2) + 1
    return min

def seat_id(ins):
    y = search(ins[:-3], 'F', 'B', 0, 127)
    x = search(ins[-3:], 'L', 'R', 0, 7)
    return y, x, y * 8 + x

assert seat_id('FBFBBFFRLR') == (44, 5, 357)
assert seat_id('BFFFBBFRRR') == (70, 7, 567)

ids = [seat_id(p)[2] for p in passes]

print(max(ids))

seen = False
for i in range(0, 1000):
    if seen and i not in ids and i - 1 in ids and i + 1 in ids:
        print('answer is', i)
        break
    if i in ids:
        seen = True
