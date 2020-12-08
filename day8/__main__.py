program = []

for l in open('day8/input.txt'):
    l = l.strip()
    if not l:
        continue
    op, arg = l.split()
    arg = int(arg)
    program.append((op, arg))

def run_program(program):
    ip = 0
    acc = 0
    visited = set()

    while True:
        if ip in visited:
            print('loop', 'ip=', ip, 'acc=', acc)
            return False, 0
        if ip == len(program):
            print('terminated', 'acc=', acc)
            return True, acc
        visited.add(ip)

        op, arg = program[ip]
        if op == 'nop':
            pass
        elif op == 'acc':
            acc += arg
        elif op == 'jmp':
            ip += arg - 1
        ip += 1

run_program(program)

for di in range(len(program)):
    if program[di][0] in ('nop', 'jmp'):
        dprogram = list(program)
        op, arg = dprogram[di]
        dprogram[di] = (dict(nop = 'jmp', jmp = 'nop')[op], arg)
        terminated, acc = run_program(dprogram)
        if terminated:
            print('answer', acc)
            break
