#1   57
#2   wyzx
#3 376
#5 230
#6 18
#7 1806
#8 13951
#9 88
#10 10
#11 19780
#12 49
#13 15
#14 680162856
#15 43
#16 4037
#17 4335 186619
#18 2198 805
#19 21
#20 719
#21 18
#22 215
#23 136
#24 1605
#25 22846113 70731
# 24816413 76831
# 28886213 89431
#  27 - 15116


# from fnmatch import*
# for x in range(323, 10**8, 323):
#     if fnmatch(str(x), "2*8?6?13"):
#         print(x, x//323)


# def f(x, y):
#    if x>y or x ==15: return 0
#    if x==y: return 1
#    if x <y: return f(x+1, y)+f(x+2, y)+f(x*2, y)
# print(f(3, 9)*f(9, 17))
# def f(a, n):
#    if a>=65 and (n == 3): return True
#    if a>=65 and n<3: return False
#    if a<65 and n==3: return False
#    if n %2==0:
#       return f(a+1, n+1)+f(a+2, n+1)+f(a*3, n+1)
#    return f(a + 1, n + 1) * f(a + 2, n + 1) * f(a * 3, n + 1)
# for s in range(1, 65):
#    if f(s, 1): print(s)

# l = []
# for n in range(3, 10001):
#    st = "5"+"2"*n
#    while "72" in st or "522" in st or "2222" in st:
#       if "72" in st:
#          st=st.replace("72", "22", 1)
#       if "522" in st:
#          st=st.replace("522", "25", 1)
#       if "2222" in st:
#          st=st.replace("2222", "5", 1)
#    su = sum(map(int, st))
#    if su==63:
#       print(n)
import sys

# def tr(n):
#    s = ""
#    while n:
#       ost = str(n%3)
#       s = ost+s
#       n//=3
#    return s
# l = []
# for n in range(0, 10000):
#    nnew = tr(n)
#    if n%3==0:
#       nn = nnew+nnew[-2:]
#
#    if n%3!=0:
#       ost = tr((n%3)*5)
#       nn = nnew+ost
#
#    r = int(nn, 3)
#    if r<=242: l.append(r)
# print(max(l))







#
# from turtle import *
# tracer(0)
# screensize(-10000, 10000)
# r = 20
# for i in range(2):
#    fd(19*r)
#    rt(90)
#    fd(10*r)
#    rt(90)
# penup()
# backward(3*r)
# rt(90)
# fd(8*r)
# lt(90)
# pendown()
# for j in range(2):
#    fd(32*r)
#    rt(90)
#    fd(12*r)
#    rt(90)
# update()
# up()
# for x in range(-30, 30):
#    for y in range(-30, 30):
#       goto(x*r, y*r)
#       dot(3, "Green")
# done()
c = 0
# from itertools import *
# for i, j in enumerate(product("АГКЛОПРУ", repeat=5)):
#    k = i+1
#    if k%2==0:
#       if j[0]!="Г" and j.count("Л")<=2: c+=1
# print(c)
#



# f = open("17 (1).txt").readlines()
# for i in f:
#    strk = [int(x) for x in i.split()]
#    mx = max(strk)
#    reccurring = [x for x in strk if strk.count(x)==2]
#    if len(reccurring)==4 and strk.count(mx)>1: c+=1
# print(c)


# from ipaddress import *
# net = ip_network("222.63.131.128/255.255.255.192")
# for i in net:
#    if bin(int(i))[2:].count("1")%5==0: c+=1
# print(c)

#
# alph = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")[0:19]
# for x in "E":
#    expression = int(f"5{x}642535",19)+int(f"78{x}11114",19)+int(f"9334{x}39",19)
#    print(expression//18)

#
# B = list(range(24, 90))
# C = list(range(47, 115))
# A = []
# for x in range(1, 100):
#    if (not(x in C) or (not(not(x in A) and (x in B)) or (not(x in C))))==False:
#       A.append(x)
# print(90-47)


from sys import *
# sys.setrecursionlimit(10**6)
# def f(n):
#    if n <=11: return 7
#    if n>11: return n-3+f(n-1)
# print(f(2022)-f(2020))
#
#
#
# with open("17 (12).txt", encoding="utf-8") as f:
#    f = [int(x) for x in f.readlines()]
#    tr = [[f[i], f[i+1], f[i+2]] for i in range(len(f)-2)]
#    minn = min([x for x in f if abs(x)%10==3 and len(str(abs(x)))==4])
# tr1 = [x for x in tr if ((abs(x[0])%10==3) + (abs(x[1])%10==3) + (abs(x[2])%10==3))<=2 and sum(x)>=minn]
#
# print(len(tr1), max(sum(x) for x in tr1))
#





# with open("24 (26).txt", encoding="utf-8") as f:
#     f = f.readline().rstrip()
# l = 0
# mx = 0
# for r in range(len(f)):
#     if f[r]=="Y":c+=1
#     if c>150:
#         if f[l]=="Y": c-=1
#         l+=1
#     if c == 150: mx = max(mx, r-l+1)
# print(mx)
#
#



#end variant
