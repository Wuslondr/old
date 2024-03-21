# from itertools import *
from functools import *
# from sys import *
from fnmatch import *
# for x, y, w, z in product(range(2), repeat=4):
#    if ((not(x) or (not(y))) and (not(x == z)) and w):
#       print(w, x, y, z)
# l = []
# for n in range(100, 1000):
#    nnew1 = int(str(n)[0]) + int(str(n)[1])
#    nnew2 = int(str(n)[1]) + int(str(n)[-1])
#    r = str(nnew1) + str(nnew2)
#    if r == "1115":
#       l.append(n)
# print(min(l))
# for j, i in enumerate(product("АГИЛМОРТ", repeat=4)):
#    i = "".join(i)
#    if i[0:2]=="ИГ":
#       print(j+1)
#       break
# s = "1"*99
# while "111" in s:
#    if "222" in s:
#       s = s.replace("222", "1", 1)
#    else:
#       s = s.replace("111", "2", 1)
# print(s)
#
# from ipaddress import *
# def f(n):
#    return str(IPv4Address(int(n.ljust(32, "0"), 2)))
# for mask in range(32):
#    net = ip_network(f"98.162.77.94/{mask}", 0)
#    if str(net.network_address) == "98.162.64.0":
#       mask = "1"*mask
#       print(f(mask))
# def f(n):
#    s = ''
#    while n:
#       ost = str(n%6)
#       s = ost + s
#       n //= 6
#    return s
# print(f(36**8+6**20-12).count('5'))
# A = []
# Q = range(30, 66) # 65
# P = range(20, 51) #50
# for x in range(200):
#    if not(not(not(x in A)) or (not(x in P) or (not(x in Q)))):
#       A.append(x)
# print(A) 50-30=20
# l = []
# @lru_cache(None)
# def f(n):
#    if n == 0: return 0
#    if n > 0 and n % 3 == 0: return f(n/3)
#    if n > 0 and (n % 3) > 0: return n%3 + f(n - (n % 3))
# for i in range(100000):
#    if f(i)==11:
#       print(i)
# #
# with open("17 (7).txt") as f:
#    f = [int(i) for i in f]
# s1 = [[f[j], f[i]] for j in range(len(f)-1) for i in range(j+1, len(f)) if (f[i]-f[j]) %45==0 and (f[j]%18==0 or f[i]%18==0)]
# s3 = [[abs(k[1]) - abs(k[0])] for k in s1]
# print(len(s1), *max(s3))
# for x in range(2023, 10**10, 2023):
#    if fnmatch(str(x), "1?493*41"):
#       print(x, x//2023)

# def f(x, y):
#    if x>y: return 0
#    if x == y: return 1
#    if x < y: return f(x+1, y) + f(x*2, y)+f(x+3, y)
# print(f(3, 12)*f(12, 16))15 42 44
# with open("zadanie24_1.txt") as f:
#    f = f.readline()
# print(max(map(len, f.replace("B", " ").replace("C", " ").split())))
# def f(a, n):
#    if a >= 46 and (n == 3): return True
#    if a >= 46 and n < 3: return False
#    if a < 46 and n == 3: return False
#    if n % 2 == 0:
#       return any([f(a+1, n+1), f(a*3, n+1)])
#    return all([f(a + 1, n + 1), f(a * 3, n + 1)])
# for s in range(1, 46):
#    if f(s, 1):
#       print(s)