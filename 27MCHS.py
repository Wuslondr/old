# f = open("27-B_23.txt") #1
# n = int(f.readline())
# summ = [0]
# for i in range(n):
#    pairs = [int(x) for x in f.readline().split()]
#    summ = [a + b for a in summ for b in pairs]
#    summ = {x%3: x for x in sorted(summ)}.values()
# print(max(x for x in summ if x % 3 != 0))

# f = open("27-B_637.txt") #2
# n = int(f.readline())
# summ = [0]
# for i in range(n):
#    pairs = [int(x) for x in f.readline().split()]
#    summ = [a + b for a in pairs for b in summ]
#    summ = {x%10: x for x in sorted(summ)}.values()
# print(max(x for x in summ if x % 10 != 5))

# f = open("27-B_814.txt") #3
# n = int(f.readline())
# summ = [0]
# for i in range(n):
#    pairs = [int(x) for x in f.readline().split()]
#    summ = {x%5: x for x in sorted([a+b for a in pairs for b in summ], reverse=True)}.values()
# print(min(x for x in summ if x%5!=0))

from itertools import *
# f = open("27B_682.txt") #4
# n = int(f.readline())
# summ = [0]
# for i in range(n):
#    trio = [int(x) for x in f.readline().split()]
#    trio = [trio[0]+trio[1], trio[1]+trio[2], trio[0]+trio[2]]
#    summ = {x%4: x for x in sorted([a+b for a in trio for b in summ])}.values()
# print(max(x for x in summ if x % 4 == 0))

# f = open("27A_2481.txt") #5
# n = int(f.readline())
# summ = [0]
# for i in range(n):
#    ch = [0] + [int(x) for x in f.readline().split()]
#    summ = {x%17: x for x in sorted([a+b for a in ch for b in summ])}.values()
# print(max(x for x in summ if x%17==0))

# f = open("27A_1877.txt")  #7, 9
# n = int(f.readline())
#
# m = [int(x) for x in f.readlines()]
# m = [[0, 0]] + [[x, x % 69] for x in list(accumulate(m))]
# mInd = [[*q, k] for k, q in enumerate(m)]
# sp = []
# for i in range(69):
#    l = []
#    for x in mind:
#       if x[1] == i: l.append([x[0], x[2]])
#    l.sort()
#    sp.append([l[-1][0]-l[0][0], l[-1][1]-l[0][1]] if len(l)>0 else [0, 0])
# print(max(sp))
#--------------------------------------------------------------
# for i in range(69):
#    temp = sorted([[a, c] for a, b, c in mInd if b == i])
#    sp.append([temp[-1][0]-temp[0][0], temp[-1][1]-temp[0][1]] if len(temp) > 0 else [0, 0])
# print(max(sp))
# {0, 1242, 37674, 47955}















