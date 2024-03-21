# with open("24_demo (4).txt") as f:
#     f = f.readline()
# c = cmax = 1
# for i in range(len(f) - 1):
#     if f[i] != f[i+1]:
#         c+= 1
#     else:
#         cmax = max(c, cmax)
#         c = 1
# print(cmax)

# for x in range(9):
#     for y in range(9):
#         s = int(f"88{x}4{y}", 9) + int(f"7{x}44{y}", 11)
#         if s % 61 == 0:
#             print(s//61)
# with open("17 (8).txt") as f:
#     f = [int(I) for I in f]
# s0 = [sorted([f[i], f[i+1], f[i+2]]) for i in range(len(f)- 2)]
# print(s0)
# s1 = [i for i in s0 if (i[2]**2)==((i[0]**2)+(i[1]**2))]
# print(s1)
#
# f = open("27-B.txt")
# n = int(f.readline())
#     # f = [list(map(int, sorted(j, key=lambda x: x != "")[1:])) for j in [i.split(" ") for i in f]]
# l = []
# s = [[0, 0, 0]]
# for i in range(n):
#     pair = [int(x) for x in f.readline().split()]
#     s = [[a1+b, a2 + (b%2==0), a3 + (b%2!=0)] for a1, a2, a3 in s for b in pair]
#     s = {x[1]-x[2]: x for x in sorted(s, reverse=True)}.values()
#     print(s)
#     s = sorted(s)[:1000]
# for k, ch, nch in s:
#     if k % 2 == 0 and ch > nch or k % 2 != 0 and nch>ch:
#         l.append(k)
# print(min(l))
# f = open("27-B_23.txt")
# listofsums = [0]
# correctsums = []
# for i in range(int(f.readline())):
#     pair = [int(i) for i in f.readline().split()]
#     listofsums = [pair1+sumbefore for pair1 in pair for sumbefore in listofsums]
#     listofsums = {x%3: x for x in sorted(listofsums)}.values()
# for sums in listofsums:
#     if sums % 3 != 0:
#         correctsums.append(sums)
# print(max(correctsums))

# f = open("27-B_637.txt")
# sums = [0]
# l = []
# for i in range(int(f.readline())):
#     pair = [int(x) for x in f.readline().split()]
#     sums = [a + b for a in pair for b in sums]
#     sums = {x%10: x for x in sorted(sums)}.values()
#
# for x in sums:
#     if x % 10 != 5:
#         l.append(x)
# print(max(l))
#
#
#
# f = open("27-A_814.txt")
# su = [0]
# l = []
# for i in range(int(f.readline())):
#     pair = [int(x) for x in f.readline().split()]
#     su = [a + b for a in su for b in pair]
#     su = {x%5: x for x in sorted(su, reverse=True)}.values()
#     print(su)
# print(min(x for x in su if x%5!=0))
#
#
# from itertools import *
# f = open("27A_682.txt")
# sums = 0
# answer = []
# for i in range(int(f.readline())):
#     a, b, c = sorted([int(x) for x in f.readline().split()])
#     sums += b + c
#     ost1 = c - a
#     ost2 = b - a
#     answer.append((ost1, i))
#     answer.append((ost2, i))
# if sums % 4 == 0:
#     print(sums)
# else:
#     answer.sort()
#     for j in range(len(answer)):
#         if (sums - answer[j][0])%4==0:
#             print(sums-answer[j][0])
# print(sums)
# print(answer)
# print((sums-53-41))
#2 peшение
# s = [0]
# n = int(f.readline())
# for i in range(n):
#     tr = [int(x) for x in f.readline().split()]
#     tri = [tr[0]+tr[1], tr[0]+tr[2], tr[1]+tr[2]]
#     s = [a+b for a in s for b in tri]
#     s = {x%4: x for x in sorted(s)}.values()
# print(max(j for j in s if j%4==0))
# f = open("27B_2481.txt")
# n = int(f.readline())
# s = [0]
# for i in range(n):
#     sol = [0] + [int(x) for x in f.readline().split()]
#     s = [a+b for a in sol for b in s]
#     s = list({x%17: x for x in sorted(s)}.values())
# print(s)
# print(max(j for j in s if j%17==0))
#
#
#
#
# from itertools import *
# f = open("27B_2900.txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]
# k=[]
# m = list(accumulate(a))
# m = [[0, 0]] + [[x%1000, x] for x in m]
# print(m)
# for i in range(1000):
#     t = [b for a, b in m if a == i]
#     k.append(max(t)-min(t) if len(t)>0 else 0)
# print(max(k))
# #
#
# with open("24 (14).txt") as f:
#     f = f.readline()
# c = cmax = 0
# a = set("ZXY")
# for x in range(len(f)-2):
#     if set(f[x]+f[x+1]+f[x+2]) == a:
#         cmax = max(c, cmax)
#         c = 0
#     else:
#         c += 1
# print(cmax-2)
# with open("27-A_2949.txt") as f:
#     f = [int(x)%10 for x in f][1:]
#     print(f)
# ost = [0]*10
# for n in f:
#     temp = ost[::]
#     temp[n] += 1
#     for i in range(10):
#         temp[i] += ost[i-n]
#     ost = temp
# print(ost[5])
# from itertools import accumulate
# f = open("27B_2900.txt")
# sp = []
# n = int(f.readline())
# m = [int(x) for x in f.readlines()]
# m = list(accumulate(m))
# m = [[0, 0]] + [[x%1000, x] for x in m]
# for i in range(1000):
#     t = [b for a, b in m if a == i]
#     sp.append(max(t)-min(t) if len(t) > 0 else 0)
# print(max(x for x in sp if x%1000==0))








