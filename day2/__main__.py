inputs = [x.strip() for x in open('day2/input.txt').readlines()]

def satisifies_pt1(cons, pw):
    num, let = cons.split(' ')
    low, hi = num.split('-')
    low, hi = int(low), int(hi)

    count = sum([1 for l in pw if l == let])
    return count >= low and count <= hi

def satisifies_pt2(cons, pw):
    num, let = cons.split(' ')
    low, hi = num.split('-')
    low, hi = int(low) - 1, int(hi) - 1

    count = sum([1 for x in [low, hi] if pw[x] == let])
    return count == 1

def count(satisifies):
    valid = 0

    for inp in inputs:
        constraint, password = inp.split(': ')
        if satisifies(constraint, password):
            valid += 1
    print(valid)

count(satisifies_pt1)
count(satisifies_pt2)
