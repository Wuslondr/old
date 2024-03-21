from itertools import *
# for x, y, w, z in product(range(2), repeat=4):
#    if not((x and y) or (y == z) or w):
#       print(w, z, y, x)
# def f(n):
#    ch = ""
#    while n:
#       ost = n % 3
#       ch = str(ost) + ch
#       n = n//3
#    return ch
# l = []
# for nj in range(1, 101):
#    nj3 = f(nj)
#    nj3 = nj3 + str(nj%3)
#    r = int(nj3, 3)
#    if r >=100:
#       l.append(r)
# print(min(l))
# for i, j in enumerate(product("АКРУ", repeat=5)):
#    if "".join(j)=="УКАРА":
#       print(i+1)
# with open("zadanie24_2.txt") as f:
#    f = f.readline()
# s1 = f.replace("D", "@").replace("L", "@").split("@")
# print(s1)
# def f(x, y):
#    if x > y or x == 18: return 0
#    if x == y: return 1
#    if x < y: return f(x + 1, y) + f(x * 2, y)
# print(f(1, 10) * f(10, 21))
# def t(a,b,n):
#    if a + b >=86 and 3: return 1
#    if a + b < 86 and n == 3 : return 0
#    if a + b >= 86 and n < 3: return 0
#    if n % 2 == 0:
#       return any([t(a+1,b,n+1), t(a*2, b, n+1), t(a, b+1, n+1), t(a, b*2, n+1)])
#    return all([t(a + 1, b, n + 1), t(a * 2, b, n + 1), t(a, b + 1, n + 1), t(a, b * 2, n + 1)])
# for s in range(1, 72):
#    if t(14, s, 1):
#       print(s)

# from fnmatch import *
# for x in range(273, 10**8, 273):
#    if fnmatch(str(x), "12??36*1"):
#       print(x, x//273)
# with open("17 (1).txt") as f:
#    f = [int(i) for i in f]
# s1 = [[f[j], f[i]] for j in range(len(f)-1) for i in range(j+1, len(f)) if (f[j] * f[i]) % 62 == 0]
# s2 = max(sum(l) for l in s1)
# print(len(s1), s2)

# def f(ns):
#    if ns == 0: return 0
#    if ns > 0 and ns%2==0: return f(ns/2)
#    if ns > 0 and ns%2!=0: return 1 + f(ns-1)
# for n in range(10000):
#    if f(n) == 11:
#       print(n)
# print(bin(4**16+2**36-8)[2:].count("1"))
# for A in range(100):
#    if all([((2*m + 3*n) > 40) or ((m < A) and (n <= A)) for m in range(100) for n in range(100)]):
#       print(A)
#       break
# from ipaddress import *
# def f(n):
#    return str(IPv4Address(int(n.ljust(32, "0"), 2)))
# for mask in range(32):
#    net = ip_network(f"111.81.200.27/{mask}", 0)
#    if str(net.network_address) == "111.81.192.0": !!!!!!!!!
#       mask = "1"*mask
#       print(f(mask))
# for q in range(1, 50):
#    for w in range(1, 50):
#       for e in range(1, 50):
#          s = "0" + "1"*q + "2"*w + "3"*e
#          while "01"in s or "02" in s or "03" in s:   !!!!!!!!
#             s = s.replace("01", "2302", 1)
#             s = s.replace("02", "10", 1)
#             s = s.replace("03", "201", 1)
#          if s.count("1") == 40 and s.count("2") == 10 and s.count("3")==8:
#             print(q)
#83bal



# print((lambda a, b: a if a > b else b)(17, 14))
# ad = [1, 2, 3]
# bd = (lambda x: x**3)
# print([bd(x) for x in ad])
# with open("27-A (1).txt") as sp:
#    k = int(sp.readline())
#    n = int(sp.readline())
#    print(k, n)
#    sp = [int(i) for i in sp]
# s1 = [[int(w), int(q)] for w, q in enumerate(sp)]
# s2 = [sorted([s1[i][1], s1[j][1], s1[l][1]]) for i in range(len(s1) - 2) for j in range(i+1, len(s1)-1) for l in range(i+2, len(s1)) if (sorted([s1[i][0], s1[j][0], s1[l][0]])[-1] - sorted([s1[i][0], s1[j][0], s1[l][0]])[0]) >= 3*81]
# s3 = [j for j in s2 if sum(j) == max([sum(i) for i in s2])]
# print(s3)


# k, n, *a = map(int, open("27-A (1).txt"))
# b = {x: a.count(x) for x in sorted(a)[::-1][:3]}
# back = m = float('-inf')
# for i in range(3*k, n):
#     back = max(back, a[i-3*k])
#     any_mx = max(x for x in b if (b[x] - (a[i] == x) - (back == x)) > 0)
#     m = max(m, back + any_mx + a[i])
# print(m)








