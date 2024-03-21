# def r12(n):
#     a = [[x+10, x1] for x, x1 in enumerate("AB")]
#     ch = ""
#     while n:
#         ost = n % 12
#         if ost > 9:
#             for i in range(len(a)):
#                 if a[i][0] == ost:
#                     ch = a[i][1]+ch
#                     n //= 12
#         else:
#             ch = str(ost) + ch
#             n //= 12
#     return ch
# l = []
# for j in range(100000):
#     nnew12 = r12(j)
#     if j % 4 == 0:
#         nnew = "2" + f"{nnew12}" + "64"
#     else:
#         nnew = nnew12 + max([i for i in nnew12])
#     r = int(nnew, 12)
#     if r > 1799: l.append(r)
# print(min(l))
import sys
# from itertools import *
# for x, y, z, w in product(range(2), repeat=4):
#     if ((not(x and (not(y))) or (z and w)) and ((not(y) or z) or (not(w) or x)))==False:
#         print(y, z, w, x)

# from fnmatch import *
# for i in range(1777, 10**10, 1777):
#     if fnmatch(str(i), "21???68?79"):
#         print(i, i/1777)

# def n23(x, y):
#     if x < y or x == 20: return 0
#     if x == y: return 1
#     if x > y: return n23(x-2, y)+n23(x//5, y)+n23(x-3, y)
# print(n23(41, 10)*n23(10, 5))

# with open("24 (15).txt") as f:
#     vowels = "EYUIOA"
#     consonant = "QWRTPSDFGHJKLZXCVBNM"
#     f = f.readline()
#     for i in vowels:
#         f = f.replace(f"{i}", "@")
#     for j in consonant:
#         f = f.replace(f"{j}", "*")
# count = maxcount = 1
# for k in range(len(f)-1):
#     if f[k] != f[k+1]:
#         count+=1
#     else:
#         maxcount = max(count, maxcount)
#         count = 1
# print(maxcount)
# from ipaddress import *
# k = 0
# for A in range(256):
#     net = ip_network(f"207.0.{A}.167/255.255.255.192", 0)
#     if all(bin(int(ip))[2:][:16].count("0")>bin(int(ip))[2:][16:].count("0") for ip in net):
#         k+=1
# print(k)
# c = 0
# from itertools import *
# for i in product("01234567", repeat=7):
#     i = "".join(i)
#     if i[0] != "0" and sum([i.count(j) for j in "0246"])==2:
#         for k in "135":
#             i=i.replace(f"{k}", "*")
#         if "*7" not in i and "7*" not in i and "77" not in i:
#             c+= 1
# print(c)
# a = sorted([i for i in "QWERTYUIOPASDFGHJKLZXCVBNM"])
# for x in "0123456789"+"".join(a[:21]):
#     if (int(f"931{x}964", 32) + int(f"4{x}51{x}1", 32) + int(f"2861{x}637", 32)) % 31 == 0:
#         print((int(f"931{x}964", 32) + int(f"4{x}51{x}1", 32) + int(f"2861{x}637", 32))//31)
#         break
# l = []
# for A in range(1000):
#     if all((x**2 + y**2 > 1024-x) or (y < -2 * x + A) for x in range(100) for y in range(100)):
#         l.append(A)
# print(min(l))

# with open("17 (9).txt") as f:
#     f = [int(x) for x in f.readlines()]
#     maxx = max([x for x in f if abs(x) % 100 == 50])
#     f = [[f[i], f[i+1], f[i+2]] for i in range(len(f)-2)]
# s0 = [x for x in f if x.count(x[0])==1 and x.count(x[1])==1 and x.count(x[2])==1 and len(str(abs(x[0])))==5 and len(str(abs(x[1])))==5 and len(str(abs(x[2])))==5]
# print(s0[:100])
# s1 = [x for x in s0 if sum(x)<=maxx]
# maxsum = max([sum(x) for x in s1])
# print(len(s1), maxsum)
from sys import *
# sys.setrecursionlimit(10**6)
# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 10: return n
#     if n >= 10: return g(f(n-1)%10)+f(g(n%10)-1)-f(n-3)
# @lru_cache(None)
# def g(k):
#     if k < 10: return k * -1
#     if k >= 10: return f(g(k-1)%10) + g(f(k-1)-1) + g(k-2)
# print(f(1111)+g(1111))
# 156
# 157
# 168
# 169
# 173
# from functools import *
# @lru_cache(None)
# def f(a, b, n):
#     if a + b >= 375 and (n == 3): return True
#     if a + b >= 375 and n < 3: return False
#     if a + b < 375 and n == 3: return False
#     if n % 2 == 0:
#         return any([f(a + 3, b, n+1), f(a, b + 3, n+1), f(a * 2, b, n+1), f(a, b*2, n+1)])
#     return all([f(a + 3, b, n+1), f(a, b + 3, n+1), f(a * 2, b, n+1), f(a, b*2, n+1)])
#
# for s in range(1, 348):
#     if f(s, 27, 1):
#         print(s)
#
#
#
#
#
# K= 0
# from ipaddress import *
# net = ip_network("123.222.111.192/255.255.255.248", 0)
# for i in net:
#     i = [int(bin(int(x))[2:]) for x in str(i).split(".")][-1]
#     if i%3 != 0:
#         K+=1
# print(K)




# f = open("24_11667.txt").readline()
# a = [[i, i+7] for i in range(len(f)-8) if f[i:i+8]=="INFINITY"]
# b = [a[j+1001][1] - a[j][0]-1 for j in range(len(a)-1001)]
# print(max(b))


# 17x35+x742M+x**3
# alf = sorted(["QWERTYUIOPASDFGHJKLZXCVBNM"])[0][:16]
# otv = []
#
# for x in "0123456789"+alf[0]:
#     if (int(f"17{x}35", 27) + int(f"{x}742M", 27) + int(f"{x}", 27)**3)%23==0:
#         otv.append(x)
# print((int(f"17{max(otv)}35", 27) + int(f"{max(otv)}742M", 27) + int(f"{max(otv)}", 27)**3) //23)
#

# f = open("9-210.txt").readlines()
# a = [[list(map(int, i.split())), j+1] for j, i in enumerate(f)]
# b = [i for i in a if i[0].count(k) for k in i[0]]
# sp = []
# f = open("9-210.txt").readlines()
# for i in range(len(f)):
#     a = [int(k) for k in f[i].split()]
#     b = [j for j in a if a.count(j)==3]
#     c = [l for l in a if a.count(l)==1]
#     print(c)
#     srpovt = sum(b)//3
#     vsex = sum(a)//7
#     if len(b)==3 and len(c)==4 and (srpovt>vsex):
#         sp.append(i+1)
# print(max(sp))
# #15958












