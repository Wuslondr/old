
from itertools import *
#
# for x, y, z in product(range(2), repeat=3):
#     if ((x==z) or (not(x) or (y and z))) == False:
#         print(y, z, x)
#
# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1.Строится двоичная запись числа N.
# 2.Yдаляется первая слева единица и все следующие непосредственно за ней нули.
# Если после этого в числе не остаётся цифр, результат этого действия считается равным нулю.
# 3.Полученное число переводится в десятичную запись.
# 4.Новое число вычитается из исходного, полученная разность выводится на экран.
# Пример. Дано число N = 11. Алгоритм работает следующим образом.
# 1.Двоичная запись числа N: 1011.
# 2.Удаляется первая единица и следующий за ней ноль: 11.
# 3.Десятичное значение полученного числа 3.
# 4.На экран выводится число 11 – 3 = 8.
# Сколько разных значений будет показано на экране автомата при последовательном
# вводе всех натуральных чисел от 100 до 3000?
# l = []
# for n in range(100, 3001):
#
#     nn = bin(n)[2:]
#     idn = [x for x in range(len(nn)) if nn[x]=="1"]
#     nnn = nn[idn[1]:] if len(idn)>1 else "0"
#
#     r1 = int(nnn, 2)
#     r = n-r1
#     l.append(r)
# print(len(set(l)))
# g = "A"
# c = 0
#
# for i in product("АБВГД", repeat=5):
#     i = "".join(i)
#     if i[0]!="А" and i[0]!=i[1] and i[1]!=i[2] and i[2]!=i[3] and i[3]!=i[4] \
#
#         c+=1
# print(c)

# В каждой строке электронной таблицы записаны три натуральных числа,
# задающих длины трёх взаимно перпендикулярных рёбер прямоугольного параллелепипеда.
# Определите, сколько в таблице троек,
# для которых у заданного ими параллелепипеда для любых трёх граней
# с общей вершиной сумма площадей двух из них больше площади третьей.
# cc = 0
# with open("modify.txt") as f:
#     f = [list(map(int, x.split())) for x in f]
# for i in f:
#     a, b, c = i
#     gr1 = a*b
#     gr2 = a*c
#     gr3 = c*b
#     s = sorted([gr3, gr2, gr1])
#     if (s[0]+s[1])>s[2]:
#         cc+=1
# print(cc)

# s = "1"+"8"*80
# while "288" in s or "3888" in s or "18" in s:
#     if "18" in s:
#         s = s.replace("18", "2",1)
#     if "288" in s:
#         s = s.replace("288", "3", 1)
#     else:
#         s = s.replace("3888", "1", 1)
# print(s)

# l = []
# for a in range(100):
#     if all(((2*x+3*y<30) or (x+y>=a)) for x in range(100) for y in range(100)):
#         l.append(a)
# print(max(l))

# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000. Определите и запишите в ответе
# сначала количество пар элементов последовательности, у которых
# сумма нечётна, а произведение делится на 3, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
# Порядок элементов в паре не важен.
# with open("17 (11).txt") as f:
#     f = [int(x) for x in f]
# cc = 0
# l = []
# for i in range(len(f)-1):
#     for j in range(i+1, len(f)):
#         if (f[i]+f[j])%2!=0 and (f[i]*f[j])%3==0:
#             l.append([f[i]+f[j]])
#             cc+=1
# print(cc, max(l))
# def f(x, y):
#     if x > y or x == 15: return 0
#     if x == y: return 1
#     if x < y: return f(x+1, y) + f(x+2, y)
# print(f(3, 9)*f(9, 20))
#
# def f(a, n):
#     if a>= 68 and (n == 3): return True
#     if a>=68 and n < 3: return False
#     if a <68 and n == 3: return False
#     if n % 2 == 0:
#         return f(a+1, n+1) or f(a+4, n+1) or f(a*5, n+1)
#     return f(a+1, n+1) and f(a+4, n+1) and f(a*5, n+1)
# for s in range(1, 68):
#     if f(s, 1):
#         print(s)
#


# def prime(n):
#     return all([n%x!=0 for x in range(2, int(n**0.5))])
#
# for i in range(45000000, 50000001):
#     n = i
#     while n%2==0: n//=2
#     q = round(n**0.25)
#     if n==q**4 and prime(q):
#         print(i)
# 45212176
# 45265984
# 46118408
# 47458321
# 48020000
# 48469444
# 50000000
# sp = [45212176,
# 45265984,
# 46118408,
# 47458321,
# 48020000,
# 48469444,
# 50000000]
# def f1(n):
#     l = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i==0:
#             l.append(n//i)
#             l.append(i)
#     l = [x for x in l if x % 2 !=0]
#     return set(l)
# a = [[len(f1(x)), x] for x in sp]
# print([x for x in a if x[0]==5])
# with open("24 (18).txt") as f:
#     f = f.readline()
#     ind = [x for x in range(len(f)) if f[x]=="N"]
#     print(ind[:10])
#     n = f[0:51]
# a = {x:n.count(x) for x in n}
# print(sorted([x for x in a.items()], key=lambda x: x[1], reverse=True))
# c = 0
# sp = 0
# f = open("26 (3).txt")
# f = [int(x) for x in f][1:]
# f2 = [x for x in f if x%2!=0]
# f1 = set(f)
#
# for i in range(len(f2)-1):
#     for j in range(i+1, len(f2)):
#         sr = (f2[i]+f2[j])/2
#         if sr in f1:
#             c+=1
#             sp = max(sr, sp)
# print(c, int(sp))
#
# f = open("27-B_2.txt")
# n = int(f.readline())
# f = [int(x) for x in f.readlines()]
# mmax = max(f)
# f1 = max([x for x in f if x%14==0])
# print(mmax*f1)
#
# s = max([x for x in f if x%7==0])
# s1 = max([x for x in f if x%2==0])
# print(s*s1)
#















# from ipaddress import *
# def f(n):
#     return str(IPv4Address(int(n.ljust(32, "0"), 2)))
# for mask in range(32):
#     net = ip_network(f"148.195.140.28/{mask}", 0)
#     if str(net.network_address)=="148.195.140.0":
#         mask = "1"*mask
#         print(sum([bin(int(x))[2:].count("1") for x in f(mask).split(".")]))
#






# with open("24_855.txt") as f:
#     f = f.readline()
# l = []
# d = {}
# for i in range(len(f)-2):
#     if f[i]+f[i+2]=="XZ":
#         d[f[i+1]] = d.get(f[i+1], 0) + 1
# print(sorted(d.items()))

#         l.append(f[i+1])
# a = sorted({x: l.count(x) for x in "QWERTYUIOPASDFGHJKLZXCVBNM"}.items(), key=lambda x: x[1], reverse=True)
# print(a)
# sp = []
# for i in f:

    # a = sorted({x: i.count(x) for x in i}.items(), key=lambda x: x[1], reverse=True)
    # print(a)
    # break

# with open("27-B_2133.txt") as f:
#     n = int(f.readline())
#     a = [int(x) for x in f.readlines()]
#     s, m, l = 0, 0, 0
#     total = [[[float("inf"), 0]]*73 for i in range(37)]
# for j in range(n):
#     x = a[j]
#     s+=x
#     if s%37 == 0 and (x+a[0])%73==0:
#         m = max(m, s)
#     if total[s%37][(73-x%73)%73][0]!= float("inf"):
#         if (s-total[s%37][(73-x%73)%73][0])>m or \
#                 (s - total[s % 37][(73 - x % 73) % 73][0])==m and




