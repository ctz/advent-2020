lines = [x.strip() for x in open('day4/input.txt').readlines()]
lines.append('')

passports = []
current = {}

def parse(line):
    d = {}
    for pair in line.split():
        k, v = pair.split(':')
        d[k] = v
    return d

for l in lines:
    if l == '':
        if current:
            print('done', current)
            passports.append(current)
            current = {}
        continue

    current.update(parse(l))

required = set('byr iyr eyr hgt hcl ecl pid'.split())

print(len([p for p in passports if required.issubset(p.keys())]))

def ishex(s):
    for x in s:
        if x not in '0123456789abcdef':
            return False
    return True

def validate_height(h):
    if h.endswith('in'):
        return 59 <= int(h[:-2]) <= 76
    elif h.endswith('cm'):
        return 150 <= int(h[:-2]) <= 193
    else:
        return False

validators = dict(
    byr = lambda v: v.isnumeric() and 1920 <= int(v) <= 2002,
    iyr = lambda v: v.isnumeric() and 2010 <= int(v) <= 2020,
    eyr = lambda v: v.isnumeric() and 2020 <= int(v) <= 2030,
    hgt = validate_height,
    hcl = lambda v: len(v) == 7 and v[0] == '#' and ishex(v[1:]),
    ecl = lambda v: v in 'amb blu brn gry grn hzl oth'.split(),
    pid = lambda v: len(v) == 9 and v.isnumeric(),
)

def valid(p, vs):
    #print('check', p)
    for k, v in vs.items():
        if k not in p or not v(p[k]):
            #print('rej', p, k, v)
            return False
    return True

print(len([p for p in passports if valid(p, validators)]))

