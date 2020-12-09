numbers = [int(x.strip()) for x in open('day9/input.txt')]

def is_window25_sum(i):
    value = numbers[i]
    window = numbers[i-25:i]
    print(window, value)
    for j, jn in enumerate(window):
        for k, kn in enumerate(window):
            if j != k and jn + kn == value:
                return True

for i in range(25, len(numbers)):
    if not is_window25_sum(i):
        print('answer =', i, '=', numbers[i])
        break

i, answer = 641, 1212510616

def find_sum_span(starti, target):
    for hi in range(starti-1, 25, -1):
        rem = target - numbers[hi]
        for lo in range(hi-1, 25, -1):
            rem -= numbers[lo]
            if rem < 0:
                break
            elif rem == 0:
                print('sum', lo, hi, numbers[lo:hi+1])
                assert sum(numbers[lo:hi+1]) == target
                return numbers[lo:hi+1]

span = find_sum_span(i, answer)
print(min(span) + max(span))
