# def fun(arg):
#     print(arg)
# a = fun("sas")
# print(a)

# def func(a, b, c):
#     print(a, b, c) #позиционные
#
# func(1, 2, 3)
#
# def func(a, b, d=None): #d - именнованый
#     print()
# func("s", "sa")

# def function(a, b):
#     print("a: ", a, "\nb: ", b)
# function("b", "a")
# l = []
# count = 0
# for n in range(0, 10000000000):
#     n_bin = str(bin(n)[2:])
#     a = [int(i) for i in str(n)]
#     if sum(a) % 2 != 0:
#         n_bin_new = n_bin + '1'
#     if sum(a) % 2 == 0:
#         n_bin_new = n_bin + '0'
#     intbin1 = int(n_bin_new, 2)
#     b = [int(z) for z in str(intbin1)]
#     if sum(b) % 2 != 0:
#         n_bin_new = str(bin(intbin1)) + '1'
#     if sum(b) % 2 == 0:
#         n_bin_new = str(bin(intbin1)) + '0'
#     intbin2 = int(n_bin_new, 2)
#     c = [int(x) for x in str(intbin2)]
#     if sum(c) % 2 != 0:
#         n_bin_new = str(bin(intbin2)) + '1'
#     if sum(c) % 2 == 0:
#         n_bin_new = str(bin(intbin2)) + '0'
#     r = int(n_bin_new, 2)
#     if 123456789 <= r <= 1987654321:
#         l.append(r)
#         print(len(l))
# c = 0
# for n in range(248456789, 248456790):
#     bin_n = str(bin(n))[2:]
#     def sumas(n):
#         a = [int(i) for i in str(n)]
#         return sum(a)
#     def chet(n):
#         bin_n = str(bin(n))[2:]
#         if sumas(n) % 2 != 0:
#             bin_n += '1'
#             return int(bin_n, 2)
#         if sumas(n) % 2 == 0:
#             bin_n += '0'
#             return int(bin_n, 2)
#     n = chet(n)
#     n = chet(n)
#     n = chet(n)
#     print(n)
# def summ(n):
#     sumi = 0
#     while n > 0:
#         sumi += n % 10
#         n = n // 10
#     return sumi
# print(summ(101))
# # print(10%10)
# print(bin(123)[2:])
# q1 = bin(123)[2:]
# q2 = int(q1[:len(q1)-3], 2)
# print((q2))
# print(q1[:len(q1)-3])
# a = int(bin(123456789)[2:][:-3], 2)
# b = int(bin(1987654321)[2:][:-3], 2)
# c = b - a - 1
# print(c)
# print((b))

# номер 4 ч 1
# for n in range(0, 99999):
#     binn = bin(n)[2:]
#     sumn = sum([int(i) for i in binn])
#     ost = sumn % 2
#     binnew = str(binn) + str(ost)
#     sumn2 = sum([int(i) for i in binnew])
#     ost2 = sumn2 % 2
#     binnew2 = binnew + str(ost2)
#     r = int(binnew2, 2)
#     if r > 97:
#         print((r))
#         break

# номер 5 ч 1
# for n in range(0, 256):
#     bun = str(bin(n)[2:].zfill(8))
#     zam = bun.replace("0", "u")
#     zam1 = zam.replace("1", "0")
#     zam2 = zam1.replace("u", '1')
#     r = int(zam2, 2) - int((bin(n)[2:].zfill(8)), 2)
#     if r == 133:
#         print((n))

# номер 6 ч 1
# l = []
# for n in range(0, 99999):
#     binn = bin(n)[2:]
#     if n % 3 == 0:
#         a = str(binn) + str(binn)[-3:]
#     if n % 3 != 0:
#         a = str(binn) + str(bin(n % 3 * 3)[2:])
#     r = int(a, 2)
#     if r <= 137:
#         l.append(r)
# print(max(l))
# nomer 1 c 1
# for i in range(100, 1000):
#     s = str(i)
#     sum1 = int(s[0]) + int(s[1])
#     sum2 = int(s[1]) + int(s[2])
#     max1 = str(max(sum1, sum2))
#     min1 = str(min(sum1, sum2))
#     sum3 = min1 + max1
#     if sum3 == '1216':
#         print(i)
#         break
# nomer2
# for i in range(100, 1000):
#     s = str(i)
#     sum1 = int(s[0]) * int(s[1])
#     sum2 = int(s[1]) * int(s[2])
#     max1 = str(max(sum1, sum2))
#     min1 = str(min(sum1, sum2))
#     sum3 = min1 + max1
#     if sum3 == '621':
#         print(i)
#         break
# nomer3
# l = []
# for i in range(1000, 10000):
#     s = str(i)
#     sum1 = int(s[0]) + int(s[1])
#     sum2 = int(s[1]) + int(s[2])
#     sum3 = int(s[2]) + int(s[3])
#     max1 = str(max(sum1, sum2, sum3))
#     min1 = str(min(sum1, sum2, sum3))
#     avg = [str(sum1), str(sum2), str(sum3)]
#     avg.remove(max1)
#     avg.remove(min1)
#     sum22 = avg[0] + max1
#     if sum22 == '1517':
#         l.append(i)
# print(max(l))

# from turtle import *
# speed(100)
# pen()
# right(90)
# for i in range(4):
#     right(60)
#     forward(2 * 23)
#     right(60)
#     forward(2 * 23)
#     right(270)
# penup()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         setpos(x * 23, y * 23)
#         dot(3)
# done()
# c = 0
# word = 'СВЕТЛАН'
# for i in word:
#     for i1 in word:
#         for i2 in word:
#             for i3 in word:
#                 for i4 in word:
#                     for i5 in word:
#                         for i6 in word:
#                             for i7 in word:
#
#                                 scl = i + i1 + i2 + i3 + i4 + i5 + i6 + i7
#                                 if scl.count('А') == 2 and scl.count('С') == 1 and scl.count('В') == 1 and \
#                                         scl.count('Е') == 1 and scl.count('Т') == 1 and scl.count('Т') == 1 and \
#                                         scl.count('Л') == 1 and scl.count('Н') == 1 and scl.count('АА') == 0:
#                                     c += 1
#
# print(c)
#Вася составляет 5-буквенные слова, в которых встречаются только буквы
# А, Б, В, Г, причём буква А появляется ровно 1 раз.
# Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
# Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
# Сколько существует таких слов, которые может написать Вася?
# c = 0
# a = "АБВГ"
# for i in a:
#     for i1 in a:
#         for i2 in a:
#             for i3 in a:
#                 for i4 in a:
#                     w = i + i1 + i2 + i3 + i4
#                     if w.count("А") == 1:
#                         c += 1
# print(c)
# for x in range(38):
#     summ = (1 * 37 ** 3 + 2 * 37 ** 2 + 3 * 37 ** 1 + x) + (4 * 37 ** 3 + x * 37 ** 2 + 5 * 37 ** 1 + 9)
#     if summ % 36 == 0:
#         print(summ // 36)
#         break
# f = '0123456789abcdefg'
# for x in f:
#     f1 = int('8' + x + '5678', 25)
#     s2 = int('457' + x + '69', 25)
#     t3 = int('145' + x + '1', 25)
#     summ = f1 + s2 + t3
#     if summ % 23 == 0:
#         print(summ // 23)
#         break
# s = ''
# n = 729 ** 7 + 3 ** 16 - 18
# while n:
#     s = str(n % 9) + s
#     n //= 9
# print(s.count('0'))
# from itertools import *
# a = list(product('12', repeat=13))
# print(a)

# sd = []
# for i in a:
#     c = ''.join(i)
#     print(c)
#     if c.count('1') == 10 and c.count('2') == 3:
#         while '11' in c:
#             if '112' in c:
#                 c = c.replace('112', '6', 1)
#             else:
#                 c = c.replace('11', '3', 1)
#         summ = c.count('1') + c.count('2')*2 + c.count('3')*3 + c.count('6')*6
#         sd.append(summ)

# from itertools import product
# al = []
# maxx = 0
# for A in range(1000):
#     for x in range(1000):
#         if ((x & 39 == 0) or ((x & 11 == 0) <= (x & A != 0))) == 0:
#             break
#     else:
#         print(A)

# P = range(20, 51)
# Q = range(30, 66)
# A = []
# for x in range(1000):
#     if (((not(x in A)) <= ((x in P) <= (not(x in Q))))) == False:
#         A.append(x)
# print(A)
# for a in range(1000):
#
#     if all(((x <= 9) <= (x*x <= a) and ((y*y <= a) <= (y <= 9))) for x in range(200) for y in range(200)):
#         print(a)


#
# for A in range(1, 1000):
#
#     if all((((x + 2*y) < A) or (y > x) or (x > 60)) for x in range(100) for y in range(100)):
#             print(A)


# def Del(n, m):
#     return n % m == 0
#
# for a in range(1, 1001):
#
#     if all((x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0)) for x in range(1, 1000)):
# #         print(a)
# P = list(range(25, 51))
# Q = list(range(32, 48))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))) == False:
#         A.remove(x)
# print(A)
# from ipaddress import *
# a = []
# net = ip_network('162.198.0.157/255.255.255.224')
#
# for ip in net:
#     print(ip)
    # if bin(int(ip)).count('1') % 2 == 0:
    #     a += '1'
    #     print(a.count('1'))
# a = str(bin(224))[2:].zfill(8), str(bin(128))[2:].zfill(8), str(bin(114))[2:].zfill(8), str(bin(142))[2:].zfill(8)
# b = [str(bin(224))[2:].zfill(8), str(bin(128))[2:].zfill(8), str(bin(64))[2:].zfill(8), str(bin(0))[2:].zfill(8)]
# print(a)
# print(b)
# print(int("11000000", 2))

# import sys
# sys.setrecursionlimit(10**6)
# def F(n):
#     if n < 11:
#         return 10
#     else:
#         return n + F(n - 1)
# print(F(2021) - F(2019))
# def F(a, b):
#     if b == 0:
#         return 0
#     if a > b:
#         return F(a - 1, b) + b
#     if a <= b and b > 0:
#         return F(a, b - 1) + a
# post = []
# c = 0
# with open("17 (1).txt") as f:
#     lest = [int(i) for i in f]
#     for x in range(len(lest) - 1):
#         for y in range(x + 1, len(lest)):
#
#             if (lest[x] % 160 != lest[y] % 160) and (lest[x] % 7 == 0 or lest[y] % 7 == 0):
#                 sim = lest[x] + lest[y]
#                 post.append(sim)
#
#                 c += 1
# print(max(post), c)

# clear_list = []
# with open("17_2024.txt") as file:
#     gen_list_for_file = [int(i) for i in file]
#     for x in range(len(gen_list_for_file) - 2):
#         max_sum_from_gen = max([int(k) for k in gen_list_for_file if abs(k) % 100 == 13])
#         summ = gen_list_for_file[x] + gen_list_for_file[x + 1] + gen_list_for_file[x + 2]
#         if (summ <= max_sum_from_gen) \
#             and (((len(str(gen_list_for_file[x])) == 3) and (len(str((gen_list_for_file[x + 1]))) == 3) and (len(str((gen_list_for_file[x + 2]))) != 3)) \
#             or ((len(str(gen_list_for_file[x])) == 3) and (len(str((gen_list_for_file[x + 1]))) != 3) and (len(str(gen_list_for_file[x + 2])) == 3)) \
#             or ((len(str(gen_list_for_file[x])) != 3) and (len(str(gen_list_for_file[x + 1])) == 3) and (len(str((gen_list_for_file[x + 2]))) == 3))):
#             clear_list.append(summ)
# print(len(clear_list), max(clear_list))

# def f(a, b, n):
#     if a + b > 40 or n > 1:
#         return n == 1
#     if n % 2 == 1:
#         if a > b:
#             return any([f(a + 1, b, n + 1),
#                         f(a + 2, b, n + 1),
#                         f(a + 3, b, n + 1), f(a, b * 2, n + 1)])
#         if a < b:
#             return any([f(a * 2, b, n + 1),
#                         f(a, b + 1, n + 1),
#                         f(a, b + 2, n + 1), f(a, b + 3, n + 1)])
#         if a == b:
#             return any([f(a + 1, b, n + 1),
#                         f(a + 2, b, n + 1),
#                         f(a + 3, b, n + 1), f(a, b + 1, n + 1),
#                         f(a, b + 2, n + 1), f(a, b + 3, n + 1)])
#
#
#     if a > b:
#         return any([f(a + 1, b, n + 1),
#                         f(a + 2, b, n + 1),
#                         f(a + 3, b, n + 1), f(a, b * 2, n + 1)])
#     if a < b:
#         return any([f(a * 2, b, n + 1),
#                         f(a, b + 1, n + 1),
#                         f(a, b + 2, n + 1), f(a, b + 3, n + 1)])
#     if a == b:
#         return any([f(a + 1, b, n + 1),
#                         f(a + 2, b, n + 1),
#                         f(a + 3, b, n + 1), f(a, b + 1, n + 1),
#                         f(a, b + 2, n + 1), f(a, b + 3, n + 1)])
# l = []
# for d in range(1000):
#     for s in range(1000):
#         if f(d, s, 0):
#             l.append(d+s)
# print(min(l))
# def f(a, b, n):
# #     if a + b >= 88 or n > 3:
# #         return n == 3
# #     if n % 2 == 1:
# #         return all([f(a + 1, b, n + 1), f(a * 3, b, n + 1), f(a, b + 1, n + 1), f(a, b * 3, n + 1)])
# #     return any([f(a + 1, b, n + 1), f(a * 3, b, n + 1), f(a, b + 1, n + 1), f(a, b * 3, n + 1)])
# # for s in range(1, 72):
# #     if f(6, s, 0):
# #         print(s)

# def f(a, b, n):
#     if a + b >= 67 or n > 3:
#         return n == 3
#     if n % 2 == 1:
#         return all([f(a + 1, b, n + 1), f(a + b, b, n + 1), f(a, b + 1, n + 1), f(a, b + a, n + 1)])
#     return any([f(a + 1, b, n + 1), f(a + b, b, n + 1), f(a, b + 1, n + 1), f(a, b + a, n + 1)])
#
#
# for s in range(1, 58):
#     if f(9, s, 0):
#         print(s)
# import sys
# sys.setrecursionlimit(10 * 6)
# def f23(x, y):
#     if x > y or x == 15:
#         return 0
#     elif x == y:
#         return 1
#     return f23(x + 1, y) + f23(x + 3, y) + f23(x * 3, y)
# print(f23(7, 14) * f23(14, 20))
#
# def f23_1(x, y, c):
#     if x > y:
#         return 0
#     if x == y and c == 1:
#         return 1
#     return f23_1(x + 1, y, c) + f23_1(x + 2, y, c) + f23_1(x * 2, y, c + 1) + f23_1(x * 3, y, c + 1)
# print(f23_1(1, 11, 0))

# def f23(x, y):
#     if y > x:
#         return  0
#     elif x == y:
#         return 1
#     return f23(x - 2, y) + f23(x - 3, y) + f23(x // 3, y)
# print(f23(20, 3))




# with open('name') as f:
#     s = f.readline().replace('()', '@')
#     k = kmax = 0
#     for i in range(len(s) - 1):
#         if s[i] == '@' and s[i + 1] == '@':
#             k += 1
#             kmax = max(k, kmax)
#         else:
#             k = 0
# print(kmax)

# with open("24_demo.txt") as f:
#     s = f.readline().replace("XYZ", "c").replace("cccc", "Q").replace("XY", "h").replace("YX", "h").replace("ZY", "h").replace("YZ", "h").replace("ZX", "h").replace("XZ", "h")
#
#     k = kmax = 0
#     for i in range(s.index("Q"), s.index("Q") + 100):
#         if len(s[i + 1]) == "h":
#             k += 2
#             break
#         else:
#             k += 1
#             break
# print(k)
# with open("inf_22_10_20_24.txt") as f:
#     k  = 0
#     for s in f:
#         if s.count("A") > s.count("E"):
#             k += 1
# print(k)
# with open("24.txt") as f:
#     sl = {}
#
#     s = f.readline()
#     for i in range(len(s) - 1):
#
#         if s[i] == "E":
#             key = s[i + 1]
#             sl[key] = sl.get(key, 0) + 1
#
#     for x in sl.items():
#         if x[1] == max(sl.values()):
#             print(x)
# with open("24 (3).txt") as f:
#     for s in f:
#         sl = {s: s.count("G") for s in f}
#     for x in sl.items():
#         if x[1] == min(sl.values()):
#             line = x[0]
#             a = {bk: line.count(bk) for bk in set(line)}
#             break
#     for el in a.items():
#         if el[1] == max(a.values()):
#             print(el)

# def dell(a):
#     l = []
#     l.append([c for c in range(2, a) if a % c == 0 and a != c])
#     return l
#
# a = {ch: dell(ch)[0] for ch in range(210235, 210301)}
# for el in a.items():
#     if len(el[1]) == 4:
#         print(el)
# for u in range(210235, 210301):
#     delll = []
#     for j in range(2, u):
#         if u % j == 0:
#             delll.append(j)
#     if len(delll) == 4:
#         print(delll)

# for i in range(2023, 10**8, 2023):
#     num = str(i)
#     if num[0] == "3" and num[2] == "1" and num[-2:] == "57":
#         print(i, i // 2023)
# for u in range(2024, 10**10, 2024):
#     st = str(u)
#     if st[0] == "1" and st[2:6] == "2157" and st[-1:] == "4":
#         print(u, u // 2024)


# with open("26_demo.txt") as f:
#     for i in f:
#         print(i)
#         s = (sorted([int(j) for j in f]))
#         a = []
#         k, mini = 1, s[-1]
#         for l in range(len(s)):
#             a.append(f"{s[l]}")
#             if sum(map(int, a)) <= 8200:
#                 print(len(a), max(map(int, a)))

# def f(n):
#     sp = []
#     fd = [2**x for x in range(1, int(n**0.5) + 1)]
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0 and d in fd:
#             sp.append(d)
#         if n//d in fd and n % d == 0:
#             sp.append(n//d)
#
#     sp = sorted(set(sp))
#     return sp
# a = [2**x for x in range(1, 30)]
# def f(n):
#     l = []
#     for d in range(1, int(n**0.5) + 1):
#         if n % d == 0:
#             l.append(d)
#             l.append(n//d)
#     l = sorted(set(l))
#     return(l)

# from fnmatch import *
# for x in range(2031*31, 10**9, 2031*31):
#     if fnmatch(str(x), "*31*65?"):
#             print(x, x//2031 if len(f(x)) in a else "")
# def f(n):
#     l = []
#     for d in range(2, int(n**0.5) + 1):
#         if n % d == 0:
#             l.append(d)
#             l.append(n//d)
#     l = sorted(set(l))
#     return len(l) == 3

#
# for x in range(600000, 600015):
#     sl = {}
#     for v in f(x):
#         if str(v)[-1] == "7" and v != 7 and v != x:
#             sl[x] = v
#             print(sl)
# a = []
# for x in range(int(123456789**0.5) + 1, int(223456789**0.5) + 1):
#     a.append(x*x)
# d = []
# for i in a:
#     if f(i):
#         d.append(i)
# print(d)



# n24 --->



# with open("24 (3).txt") as f:
#     s = {st: st.count("G") for st in f if st.count("G") < 25}
#     k, kmax = 0, 0
#     for i in s.items():
#         i = i[0]
#         for j in range(len(i) - 1):
#             for J in range(1, len(i)):
#                 if i[j] == i[J]:
#                     k = J - j
#                     kmax = max(k, kmax)
#                 else:
#                     k = 0
# print(kmax)
# with open("24 (4).txt") as f:
#     kmax = 0
#     for s in f:
#         s = s.split("A")
#         for i in range(len(s) - 1):
#
#             kmax = max(len(s[i]) + len(s[i+1]) + 1, kmax)

# print(kmax)


# s = open('24 (7).txt').readline().split('D')[1:-1]
# mx = 0
# count = 1
# for i in range(len(s)):
#     if s[i].count('O') <= 2:
#         count += len(s[i]) + 1
#         mx = max(mx, count)
#     else:
#         count = 1
# print(mx)
# with open("24 (9).txt") as f:
#     s = f.readline()
#     y = [i for i in range(len(s)) if s[i] == "Y"]
#     print(max(y[i + 151] - y[i] - 1 for i in range(len(y) - 151)))

# s = open("1_24.txt").readline().replace("A", "@").replace("B", "@").replace("C", "@")
# k = kmax = 1
# for i in range(len(s) - 1):
#     if s[i] + s[i + 1] != "@@":
#         k += 1
#         kmax = max(k, kmax)
#     else:
#         k = 1
# print(kmax)

# def n25(m, n):
#     return 2 ** m * 3 ** n
#
#
# ans = []
# for m in range(0, 30, 2):
#     for n in range(1, 30, 2):
#         if int(400_000_000**0.5)+1 <= int(n25(m, n)**0.5)+1 <= int(600_000_000**0.5)+1:
#             ans.append(n25(m, n))
# print(sorted(ans))

# def nech(n):
#     return all(n % i != 0 for i in range(2, n))
# x = 45000000
# y = 50000000
# for j in range(1, y):
#     if nech(j):
#         l = j ** 4
#         while l <= y:
#             if l >= x and l <= y:
#                 print(l)
#             l *= 2
# def c(n):
#     ot = ''
#     while n:
#         ost = n % 7
#         ot = str(ost) + ot
#         n //= 7
#     return ot
#
# print(str(c(49**6 + 7**19 -21)).count("0"))

# P = list(range(12, 63))
# Q = list(range(52, 93))
# A = []
# for x in range(10000):
#     if ((not(not(x in A) and (x in P))) or (x in Q)) == False:
#         A.append(x)
# print(A)

# def f16(n):
#     if n == 0:
#         return 0
#     if n % 3 == 0 and n > 0:
#         return n + f16(n - 3)
#     if n % 3 > 0:
#         return n + f16(n - (n % 3))
# print(f16(26))

# with open("17 (2).txt") as f:
#     k = kmax = 0
#     sumn = -20000
#     s = [int(i) for i in f]
#     for i in range(len(s) - 1):
#         if (s[i] % 3 == 0) or (s[i + 1] % 3 == 0):
#             k += 1
#             sumn = max(sumn, s[i] + s[i + 1])
# print(k, sumn)


# def f(a, n):
#     if a >= 100 or n > 4:
#         return n == 2 or n == 4
#     if n % 2 == 0:
#         return all([f(a + 1, n + 1), f(a ** 2,n + 1)])
#     return any([f(a + 1, n + 1), f(a ** 2,n + 1)])
# for s in range(1, 99):
#     if f(s, 0):
#         print(s)
# def f(x, y):
#     if x > y or x == 31:
#         return 0
#     if x == y:
#         return 1
#     return f(x + 1, y) + f(x * 2, y)
# print(f(2, 15) * f(15, 35))


#
# i = ">" + "1"*26 + "2" * 10 + "3"*14
# c = str(i)
# while ">1" in i or ">2" in i or ">3" in i:
#     if ">1" in i:
#         i = i.replace(">1", "22>")
#     if ">2" in i:
#         i = i.replace(">2", "2>")
#     if ">3" in i:
#         i = i.replace(">3", "1>")
# print(i.count("1") + i.count("2") * 2 + i.count("3")*3)


def simple(n):
    return all([n % i != 0 for i in range(2 , n)])

def alg(s):
    while not ("00" in s):
        s = s.replace("02", "101", 1)
        s = s.replace("11", "2", 1)
        s = s.replace("012", "30", 1)
        s = s.replace("010", "00", 1)
    return sum(map(int, s))

for n in range(51, 101):
    variants = ["0" + "2" * n + "1" * 100 + "0",
                "0" + "1" * 100 + "2" * n + "0",
                "0" + "12" * n + "1" * (100 - n) + "0",
                "0" + "21" * n + "1" * (100 - n) + "0",
                "0" + "1" * (100 - n) + "12" * n + "0",
                "0" + "1" * (100 - n) + "21" * n + "0"]
    for s in variants:
        if simple(alg(s)):
            print(n)
            exit()
# b = list(range(10, 41))
# A = []
# for x in range(1, 100):
#     if (x in A) or ((x in b) <= (not(x % 6 == 0))) == False:
#         A.append(x)
# print(A)

# print(co)
# import sys
# sys.setrecursionlimit(10**6)
# def f(x, y, n):
#     if n == 3 and x + y >= 61: return True
#     if n < 3 and x + y >= 61: return False
#     if n == 3 and x + y <= 61: return False
#     else:
#         if n % 2 == 0:
#             return f(x + 1, y, n + 1) or f(x * 4, y, n + 1) or f(x, y + 1, n + 1) or f(x, y * 4, n + 1)
#         return f(x + 1, y, n + 1) and f(x * 4, y, n + 1) and f(x, y + 1, n + 1) and f(x, y * 4, n + 1)
# for s in range(1, 58):
#     if f(3, s, 0):
# #         print(s)
# from itertools import *
# for y, w, z, x in product(range(2), repeat=4):
#     if ((not(x) or y) and (y == (not(z))) and (z or w)):
#         print(x, w, z, y)


# for n in range(1000, 10000):
#     sp = []
#     sum12 = int(str(n)[0]) + int(str(n)[1])
#     sum23 = int(str(n)[1]) + int(str(n)[2])
#     sum34 = int(str(n)[2]) + int(str(n)[3])
#     sp.append(sum12)
#     sp.append(sum23)
#     sp.append(sum34)
#     sp = sorted(sp)
#     sp.pop(0)
#     sp = map(str, sp)
#     sp = ''.join(sp)
#     if sp == "613":
#         print(n)
# # for i, j in enumerate(product("АОУ", repeat=5)): #('У', 'О', 'У', 'А', 'У')
#     print(i, j)
# a = "1"*77
# while "11111" in a:
#     a = a.replace("222", "1", 1)
#     a = a.replace("111", "2", 1)
#     print(a)
# P = list(range(5, 31))
# Q = list(range(14, 24))
# A = list(range(1000))
# for x in range(1000):
#     if not(not((x in P) == (x in Q)) or (not(x in A))):
#         A.remove(x)
# print(A)
# from functools import *
# @lru_cache
# def f(n):
#     if n == 1: return 1
#     if n > 1: return f(n - 1) + 2 ** (n - 1)
# print(f(12))
# with open("17 (3).txt") as f:
#     s = [int(i) for i in f]
#     s1 = [[s[i], s[j]] for i in range(len(s) - 1) for j in range(i + 1, len(s)) if sum([s[i], s[j]]) % 2 != 0 and s[i] * s[j] % 5 == 0]
#     s2 = max([sum(i) for i in s1])
#     print(len(s1), s2)
# a = []
# fd = []
# def f(a, b, n):
#     if a + b >= 61 and (n == 3 or n == 5): return True
#     if n == 5 and a + b < 61: return False
#     if n < 5 and a + b >= 61: return False
#     if n % 2 == 0:
#         return any([f(a + 1, b, n + 1), f(a * 4, b, n + 1), f(a, b + 1, n + 1), f(a, b * 4, n + 1)])
#     return all([f(a + 1, b, n + 1), f(a * 4, b, n + 1), f(a, b + 1, n + 1), f(a, b * 4, n + 1)])
# for s in range(1, 58):
#     if f(3, s, 1):
#         a.append(s)
# def f1(a, b, n):
#     if a + b >= 61 and (n == 3): return True
#     if n == 3 and a + b < 61: return False
#     if n < 3 and a + b >= 61: return False
#     if n % 2 == 0:
#         return any([f1(a + 1, b, n + 1), f1(a * 4, b, n + 1), f1(a, b + 1, n + 1), f1(a, b * 4, n + 1)])
#     return all([f1(a + 1, b, n + 1), f1(a * 4, b, n + 1), f1(a, b + 1, n + 1), f1(a, b * 4, n + 1)])
# for d in range(1, 58):
#     if f1(3, d, 1):
#         fd.append(d)
# print(a)
# print(fd)
# def f(x, y):
#     if x > y: return False
#     if x == y: return 1
#     else:
#         return f(x + 2, y) + f(x * 5, y)
# print(f(2, 50))
# with open("27-A.txt") as f:
#     n = int(f.readline())
#     print(n)
#     a = [int(s) for s in f]
#     a1 = {(a[i], a[i+1]): sum([a[i], a[i+1]]) for i in range(len(a) - 1)}
#     for x in a1.items():
# lefts = [0 for i in range(30)]
# print(lefts)
# a = str(bin(119))[2:].zfill(8), str(bin(167))[2:].zfill(8), str(bin(50))[2:].zfill(8), str(bin(77))[2:].zfill(8)
# b = [str(bin(119))[2:].zfill(8), str(bin(167))[2:].zfill(8), str(bin(48))[2:].zfill(8), str(bin(0))[2:].zfill(8)]
# print(a)
# print(b)
# #
# def f(n):
#     s = set([i for i in range(2, int(n**0.5)) if n % i == 0])
#     s1 = set([n//i for i in s])
#     s2 = s | s1
#     return sorted(list(s2))
# for i in range(300000001, 300000100):
#     if len(f(i)) > 4:
#         print(f(i)[-5])
#
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество групп из идущих подряд не менее 10 символов,
# которые начинаются и заканчиваются буквой A и не содержат других букв A
# (кроме первой и последней) и букв B.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# with open("24 (11).txt") as f:
#     f = "".join(f.readlines())
# c = 0
# s = [j for j in range(len(f)) if f[j] == "A"]
# for y in range(len(s) - 1):
#     if s[y+1] - s[y] >= 9 and f[s[y]:s[y+1] + 1].count("B") == 0:
#         c += 1
# print(c)
# from ipaddress import *
# def f(n):
#     return str(IPv4Address(int(n.ljust(32, "0"), 2)))
# for mask in range(32):
#     net = ip_network(f"119.167.50.77/{mask}", 0)
#     if str(net.network_address) == "119.167.48.0":
#         mask = f("1"*mask)
#         mask = mask.split(".")
#         print(mask)
#
# with open("26.txt") as f:
#     f = f.readlines()[1:]
# nc = 0
# kc = 0
# s = [i.split(" ") for i in f]
# s1 = sorted([[int(k[0]), int(k[1])] for k in s])
# s2 = [s1[i] for i in range(len(s) - 1) if s1[i][0] < s1[i+1][1]]
# for i in range(len(s1) - 1):
#     for y in range(i + 1, len(s1)):
#         if s1[i][0]<s1[y][1]:
#
# В текстовом файле содержится некоторое количество натуральных чисел.
# Определите и запишите в ответ максимальную сумму трех чисел,
# чтобы любые два числа находились на расстоянии не менее К друг от друга.
# Входные данные.
# Первая строка файла содержит число k- расстояние между элементами,
# вторая строка файла содержит содержит количество элементов в файле.
# from ipaddress import *
# def f(n):
#     return str(IPv4Address(int(n.ljust(32, "0"), 2)))
# for mask in range(32):
#     net = ip_network(f"119.167.50.77/{mask}", 0)
#     if str(net.network_address) == "119.167.48.0":
#         mask = "1"*mask
#         print(f(mask))
#
