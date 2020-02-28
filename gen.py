begin = int(input('first task number = ')) - 1
end = int(input('last task number = '))
N = int(input('number of students = '))
tasks = [list()] * begin

print('processing tasks from', begin, 'to', end)
with open('pin', 'r') as fin:
    pi = fin.readline().rstrip()
    for task in range(begin, end):
        kek = list()
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                fi = task * 300 + 3 * 35 + i - 1
                fj = task * 300 + 3 * 35 + j - 1
                if pi[fi] == pi[fj]:
                    kek.append((i, j))
        tasks.append(kek)
d = [tuple() for i in range(N)]
with open('stud.txt', 'r') as p:
    for i in range(N):
        line = p.readline().rstrip().split()
        d[int(line[0]) - 1] = (line[1], line[2])
st = [set() for i in range(N)]
st1 = [0] * N
with open('ans.txt', 'w') as res:
    print('YOUR TASKS:', file=res)
    with open('pin', 'r') as fin:
        pi = fin.readline().rstrip()
        for s in range(N):
            print(*d[s], ':', end=' ', file=res)
            for task in range(begin, end):
                f = pi[task * 300 + 3 * 35 + s]
                print(f, end=' ', file=res)
            print(file=res)
    print(file=res)
    print('=' * 60, file=res)
    print(file=res)
    for task in range(begin, end):
        for pair in tasks[task]:
            print('task ' + str(task + 1) + ': ', *d[pair[0] - 1], 'and', *d[pair[1] - 1], file=res)
            st[pair[0] - 1].add(task)
            st[pair[1] - 1].add(task)
            st1[pair[0] - 1] += 1
            st1[pair[1] - 1] += 1
    print(file=res)
    print('=' * 60, file=res)
    print(file=res)
    print('similarities for each student:', file=res)
    for s in range(23):
        print('stud', *d[s], 'total num of tasks:', str(len(st[s])) + ',', 'total similarities:', st1[s], file=res)
print('PROCESS DONE SUCCESSFULLY!')
