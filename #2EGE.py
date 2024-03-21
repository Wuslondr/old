import sys
from itertools import *
# for x, y, z, w in product(range(2), repeat=4):
#    if (((not(y) or w) == (not(x) or (not(z)))) and (x or w)) == True:
#       print(y, z, w, x)
# print("-----------")
# for x, y, z, w in product(range(2), repeat=4):
#    if (((not(y) or w) == (not(x) or (not(z)))) and (x or w)) == False:
#       print(y, z, w, x)
# l = []
# for n in range(1, 1000):
#    nbin = bin(n)[2:]
#    nbinnew = nbin + str(sum(map(int, nbin))%2)
#    nbinnew2 = nbinnew + str(sum(map(int, nbinnew))%2)
#    r = int(nbinnew2, 2)
#    l.append(r)
# for i in sorted(l):
#    if i > 97:
#       print(i)
#       break
# c = 0
# for i in product("СВЕТА", repeat=5):
#    if i.count("С") >= 1:
#       c += 1
# print(c)
# def f(x, y):
#    if x > y or x == 10: return 0
#    if x == y: return 1
#    if x < y: return f(x + 1, y) + f(x *2, y)
# def f1(x, y):
#    if x > y or x == 9: return 0
#    if x == y: return 1
#    if x < y: return f1(x + 1, y) + f1(x * 2, y)
# print(f(1, 9) * f(9, 20))
# print(f1(1, 10)*f1(10, 20))
# with open("24_demo (3).txt") as f:
#    f = f.readline()
# f = f.replace("Z", "@").replace("Y", "@").split("@")
# f = max([len(i) for i in f if i.count("X")>0])
# print(f)
# print(max((map(len, open("24_demo (3).txt").readline().replace("Z", "@").replace("Y", "@").split("@")))))

# def f(n):
#    s1 = {i for i in range(1, int(n**0.5)+1) if n % i == 0}
#    s2 = {n//i for i in s1}
#    return s1.union(s2)
# print(f(100))
# l = []
# for i in range(31261400, 312652000):
#    if len(f(i)) == 6:
#       l.append(i)
# print(max(l))
from sys import *
# sys.setrecursionlimit(10**6)
# from functools import *
# @lru_cache(None)
# def f(n):
#    if n <=1:return 0
#    if n > 1 and n %2!=0: return f(n-1) + 3*n**2
#    if n > 1 and n % 2 == 0: return n/2 + f(n-1)+2
# print(f(49))
# def f(n):
#    st = ""
#    while n:
#       ost = n % 3
#       st = str(ost) + st
#       n = n // 3
#    return st
# print(str(f(9**11*3**20 - 3**9 - 27)).count("2"))
# a = str(f(9**11*3**20 - 3**9 - 27))
# b = {i[1] for i in {key: a.count(key) for key in a}.items()}
# def f(a, n):
#    if a >= 69 and (n == 3): return True
#    if a >= 69 and n < 3: return False
#    if a < 69 and n == 3: return False
#    if n % 2 == 0:
#       return any([f(a*5, n + 1), f(a+1, n+1), f(a+4, n+1)])
#    return all([f(a * 5, n + 1), f(a + 1, n + 1), f(a + 4, n + 1)])
# for s in range(1, 69):
#    if f(s, 1):
#       print(s)
#
# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар
# элементов последовательности
# , для которых произведение элементов кратно 26,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента
# последовательности. Порядок элементов в паре не важен.

# with open("17 (6).txt") as f:
#    f = [int(i) for i in f]
# s0 = [[f[i], f[j]] for i in range(len(f)-1) for j in range(i+1, len(f)) if (f[i]*f[j])%26==0]
# print(len(s0), max(map(sum, s0)))
# for a in range(200):
#    for x in range(200):
#       for y in range(200):
#          if ((x > a) or (y>x) or ((2*y+x)<110)) and x == y == a:
#             print(a) -
# print(bin(240)[2:])
# print(bin(200)[2:])
# s = ">"+"1"*11 + "2"*12 + "3"*30
# while ">1" in s or ">2"in s or ">3" in s:
#    if ">1" in s:
#       s = s.replace(">1", "22>", 1)
#    if ">2" in s:
#       s = s.replace(">2", "2>", 1)
#    if ">3" in s:
#       s = s.replace(">3", "1>")
# print(s)
# print(sum(map(int, "2222222222222222222222222222222222111111111111111111111111111111")))

#
#88
