import sys

# 1. 같은 눈 세개 : 10,000 + 같은 눈 * 1,000
# 2. 같은 눈 두개 : 1,000 + 같은 눈 * 100
# 3. 모두 다른 눈 : 그 중 가장 큰 눈 * 100

# a, b, c = map(int, input().split())

# if a == b == c: print(10000 + a * 1000)
# else:
#     if a==b or a==c: print(1000 + a * 100)
#     elif b==c: print(1000 + b * 100)
#     else: 
#         list = [a,b,c]
#         print(max(list)*100)

# lst = sorted(list(map(int, input().split())))

# if len(set(lst)) is 1:
#     print(10000 + lst[0]*1000)
# elif len(set(lst)) is 2:
#     print(1000 + lst[1]*100)  # pick middle
# else:
#     print(lst[2]*100)

# 생성자 없는 수 구하기
# a = [x for x in range(0,10001)]
# for i in range(0,10001):
#     result = i
#     for j in str(i):
#         result += int(j)
#     if result in a:
#         a.remove(result)
# print(*a, sep="\n")

#한수 개수 구하기
# a = input()
# result = []
# for i in range(97, 123):
#     if chr(i) in a:
#         result.append(a.index(chr(i)))
#     else:
#         result.append(-1)
# print(*result, sep=" ")



a = int(input())
current = 1
plus = 5
#분모
parent = 1
#분자
child = 1
count = 1
#a의 범위 구하기
while a > current:
    current += plus
    plus += 4
    parent += 2
parent_copy = parent
#분수 구하기
while a != current:
    if count >= parent_copy:
        child -= 1
        if count > parent_copy:
            parent += 1
    else:
        parent -= 1
        child += 1
    count += 1
    current -= 1
print(f'{child}/{parent}')