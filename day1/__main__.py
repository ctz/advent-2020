inputs = [int(x.strip()) for x in open('day1/input.txt').readlines()]
for i in inputs:
    for j in inputs:
        if i + j == 2020:
            print(i * j)
