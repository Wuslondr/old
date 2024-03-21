import sys
# from itertools import *
# for x, y, z, w in product(range(2), repeat=4):
#    if not(y and (x or z) or (not(y or z)) or w):
#       print(x, y, w, z)
# print(1783500//1000)
# l = []
# for n in range(200000):
#    nbin = bin(n)[2:]
#    if n % 2 == 0:
#       nbin= nbin+nbin[-2:]
#    if n % 2 != 0:
#       nbin = "1"+nbin+"0"
#    r = int(nbin, 2)
#    if r < 100:
#       l.append(n)
# print(max(l))
# c = 0
# for i in product(range(9), repeat=5):
#    if (str(i[0])!="0") and (str(i).count("5")==1) and all([i[j]!=i[j+1] for j in range(4)]):
#       c+=1
# print(c)
# from ipaddress import *
# net = ip_network("192.168.32.48/255.255.255.240")
# c = 0
# for i in net:
#    j = [bin(int(k))[2:] for k in str(i).split(".")]
#    k = j[0]+j[1]+j[2]+j[3]
#    if bin(int(i))[2:].zfill(32).count("1")%2!=0:
#       c+=1
# print(c)
# l = []
# for n in range(3, 10001):
#    s = "3"+"5"*n
#    while "333" in s or "555" in s:
#       if "555" in s:
#
#          s = s.replace("555", "3", 1)
#       else:
#          s = s.replace("333", "5", 1)
#    l.append(sum(int(x) for x in s))
# print(max(l))
# def f(n):
#    s = ""
#    while n:
#       ost = n % 9
#       s = str(ost) + s
#       n //=9
#    return s
# g = f(2*729**333+2*243**334-81**335+2*27**336-2*9**337-338)
# s = 0
# for i in range(1, 9):
#    s += g.count(f"{i}")
# print(g)
# print(s)
#
#
# from fnmatch import *
# for i in range(98591, 10**12, 98591):
#    if fnmatch(str(i), "12?3*456??9"):
#       print(i, i//98591)
# with open("24_12254.txt") as f:
#    f = f.readline()
#    print("RS"+17*"RSQ"+"SQ" in f)
# c = cmax = 0
# s = f.replace("RSQ", "*")
# for i in range(len(s)):
#    if s[i]=="*":
#       c += 1
#       if c == 17:
#          print(s[i - 21:i + 5])
#    else:
#       cmax = max(c, cmax)
#       c = 0
# print(len("*****************"))
# def f(x, y):
#    if x > y or x == 16: return 0
#    if x == y: return 1
#    if x < y: return f(x**2, y) + f(x+1, y)+f(x+3, y)
# print(f(3, 20)*f(20, 26))
# import sys
# sys.setrecursionlimit(10**6)
# from functools import *
# @lru_cache(None)
# def f(n):
#    if n <= 3: return 1
#    if n > 3: return (n+3)*f(n-2)
# print(f(2028)/f(2024))
# l = []
# for A in range(2000):
#    if all((x&A==0) or (not(x&37==0)) or (not(x&12==0)) for x in range(2000)):
#          l.append(A)
# print(max(l))
# with open("17_12249.txt") as f:
#    f0 = [int(x) for x in f.readlines()]
#    m = max(k for k in f0 if str(k)[-1]=="3" and len(str(k))==5)
#
#    f = [[f0[j], f0[j+1], f0[j+2]] for j in range(len(f0)-2)]
# s = [x for x in f if len([y for y in x if str(y)[-1]=="3"])>0]
# s1 = [sum(x) for x in s if sum(x)<=m]
# print(len(s1), max(s1))
# def f(a, n):
#    if a >= 301 and (n == 3): return True
#    if a >= 301 and n < 3: return False
#    if a < 301 and n == 3: return False
#    52
# 53
# 54
# 58
# 59
# 60
#    if n % 2 == 0:
#       return any([f(a+3, n+1), f(a*5, n+1)])
#    return all([f(a + 3, n + 1), f(a * 5, n + 1)])
# for s in range(1, 301):
#    if f(s, 1):
#       print(s)

#Шастин ЕГКР 88 баллов (22 не увидел еще одну возможность с пар проц),(9 долго т.к. мало опыта на экселе)









