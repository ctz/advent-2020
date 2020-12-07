rules = {}

for rule in open('day7/input.txt'):
    colour, contents = rule.strip().split(' bags contain ')
    contents = contents.rstrip('.').split(', ')
    makeup = {}
    for c in contents:
        nr, ccolour = c.split(' ', 1)
        if nr != 'no':
            words = ccolour.split(' ')
            ccolour = words[0] + ' ' + words[1]
            makeup[ccolour] = int(nr)
    rules[colour] = makeup

def add_bags(outer_bags, current):
    for outer, contents in rules.items():
        if current in contents:
            outer_bags.add(outer)

outer_bags = set()
add_bags(outer_bags, 'shiny gold')

done = -1
while done < len(outer_bags):
    done = len(outer_bags)
    for s in [key for key in rules if any(colour in rules[key].keys() for colour in outer_bags)]:
        outer_bags.add(s)

print(outer_bags)
print(len(outer_bags))

def count_contains(col, depth=0):
    assert col in rules
    print(' '*depth, col)
    total = 0
    for ccolour, count in rules[col].items():
        print(' '*depth, '-', ccolour, count)
        total += (1 + count_contains(ccolour, depth=depth+4)) * count
    print(' '*depth, '=', total)
    return total


print(count_contains('shiny gold'))
