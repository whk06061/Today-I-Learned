import sys
#sys.stdin = open("input.txt", "rt")
a = []
result = True
for _ in range(9):
    tmp = list(map(int, input().split()))
    a.append(tmp)

for i in range(0,9,3):
    tmp = []
    for j in range(i, i+3):
        for k in range(0,3):
            tmp.append(a[j][k])
    tmp = set(tmp)
    if len(tmp) != 9:
        result = False
        break

if result == True:
    for i in range(0,9,3):
        tmp = []
        for j in range(i, i+3):
            for k in range(3,6):
                tmp.append(a[j][k])
        tmp = set(tmp)
        if len(tmp) != 9:
            result = False
            break

if result == True:
    for i in range(0,9,3):
        tmp = []
        for j in range(i, i+3):
            for k in range(6,9):
                tmp.append(a[j][k])
        tmp = set(tmp)
        if len(tmp) != 9:
            result = False
            break

if result == True:
    print("YES")
else:
    print("NO")