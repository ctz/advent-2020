import functools
import operator

map = [list(x.strip()) for x in open('day3/input.txt').readlines()]

def lookup(x, y):
    return map[y][x % len(map[y])]

def walk(dx, dy):
    x, y = 0, 0

    trees = 0
    while y < len(map):
        if lookup(x, y) == '#':
            trees += 1
        x += dx
        y += dy

    return trees

print(walk(3, 1))
answers = [
    walk(1, 1),
    walk(3, 1),
    walk(5, 1),
    walk(7, 1),
    walk(1, 2)
]
print(answers)
print(functools.reduce(operator.mul, answers, 1))
