def dividers(n):
    l = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0: l+=[i, n//i]
    return sorted(set(l))




# a = [int(x) for x in open("27990_B.txt").readlines()]
# kk = k2 = k31 = k62 = 0
#cB=0
# for x in range(len(a)):                          №27990
#     if a[x]%62==0: cB+=kk
#     elif a[x]%31==0: cB+=k2
#     elif a[x]%2==0: cB+=k31           from random import *
#     else: cB+=k62                     a = [randint(1, 1000) for i in range(n)]
#     kk+=1
#
#     if a[x]%62==0: k62+=1
#     if a[x]%31==0: k31+=1
#     if a[x] % 2 == 0: k2+=1
# print(cB)




# count = 0
# f = open("27B_2720.txt")
# n = int(f.readline())
# k = 0
# k7=nk7=0
# f = [int(x) for x in f.readlines()]               №2720
# for i in range(n):
#     if f[i]%7==0: count+=k
#     elif f[i]%7!=0: count+=k7
#     k+=1
#     if f[i] % 7 == 0: k7 += 1
#     if f[i] % 7 != 0: nk7 += 1
# print(count)


# f = open("27B_2721.txt").readlines()
# a = [int(x) for x in f][1:]
# kk = k13 = k5 = k65 = 0
# c = 0
# cc= 0
# for i in range(len(a)):                           №2721
#     x = a[i]
#     if x%65==0: c+=kk
#     elif x%5==0: c+=k13+k65
#     elif x%13==0: c+=k5+k65
#     else: c+= k65
#     kk+=1
#     if x%65==0: k65+=1
#     elif x%5==0: k5+=1
#     elif x%13==0: k13+=1
# print(c)




# f = open("27B_2722.txt").readlines()
# c = 0
# a = [int(x) for x in f][1:]
# #5->6
# #5->10
# #10->17                                           №2722
# k5ch = k5nch = kch = knch = 0
# for i in range(len(a)):
#     x = a[i]
#     if x%5 == 0 and x%2 == 0: k5ch+=1
#     elif x%5 == 0 and x%2!=0: k5nch+=1
#     elif x%5 != 0 and x%2==0: kch+=1
#     elif x % 5 != 0 and x % 2 != 0: knch+=1
# print(k5nch*kch + k5nch*k5ch + k5ch*knch)






# f = open("27B_2724.txt")
# n = int(f.readline())
# ost131 = [0]*131
# count = 0                                         №2724
# for i in range(n):
#     x = int(f.readline())
#     ost131[(x % 131) % 131] += 1
#     if x%131 == 0: count+=ost131[0] - 1 if ost131[0]!=0 else 0
#     else:
#         count+=ost131[131-(x%131)%131]
# print(count)



# f = open("27B_2733.txt")
# n = int(f.readline())
# print(n)
# b = 50000                             №2733 answer B not correct(< na 20)
# ost80 = [0]*80
# os80 = [0]*80
# count = 0
# for i in range(n):
#     x = int(f.readline())
#     if x>b:
#         ost80[(x%80)%80]+=1
#     if x<= b: os80[(x%80)%80]+=1
#
#     if x%80==0 and x>b: count+=ost80[0] + os80[0] - 1 if ost80[0]!=0 else 0
#     if x%80==0 and x<=b: count+=ost80[(x%80)%80] - 1 if os80[(x%80)%80]!=0 else 0
#     if x%80!=0 and x>b: count+=ost80[80 - ((x%80)%80)] + os80[80 - ((x%80)%80)]
#     if x%80!=0 and x<=b: count+= ost80[80 - ((x%80)%80)]
# print(count)



# f = open("27B_2726.txt")
# n = int(f.readline())                             №2726
# a =[int(x) for x in f.readlines()]
# s = list({x%2: x for x in sorted(a)}.values())
# print(s[0]+s[1])


# f = open("27B_2727.txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]
# smin = float("inf")                               №2727
# for i in range(n-1):
#     for j in range(i+1, n):
#         if (a[i]*a[j])%31==0:
#             smin = min(smin, a[i]*a[j])
# print(smin)
# print(min([x for x in a if x%31==0])*min([x for x in a]))



                                #complete search

# f = open("27A_2728.txt")
# n = int(f.readline())
# # ssmax = float("-inf")
# a = [int(x) for x in f.readlines()]               №2728
# for i in range(n-1):
#     for j in range(i+1, n):
#         if (a[i]%23 ==0 or a[j]%23==0) and (a[i]+a[j])%2==0:
#             ssmax = max(smax, a[i]+a[j])
#
# print(ssmax)

                                #First way FileB: logical
# n23 = max([x for x in a if x%23==0])
# smax = float("inf")
# sum23 = sum(sorted([x for x in a if x%23==0], reverse = True)[:2])
# if n23%2==0:
#     smax = max(n23+max([x for x in a if x%2==0]), sum23)             №2728
# else:
#     smax = max(n23+max([x for x in a if x%2!=0]), sum23)
# print(smax)

                                #Second way FileB: KABANOV.com
# f = open("27B_2728.txt")
# n = int(f.readline())
# k23_0, k23_1, k0, k1 = [], [], [], []
# for i in range(n):                                     №2728
#     x = int(f.readline())
#     if x%23==0 and x%2 == 0: k23_0.append(x)
#     elif x % 23 == 0 and x % 2 != 0: k23_1.append(x)
#     elif x % 23 != 0 and x % 2 == 0: k0.append(x)
#     elif x % 23 != 0 and x % 2 == 0: k1.append(x)
# l = sorted(k23_0)[-2:]+sorted(k23_1)[-2:]+sorted(k0)[-2:]+sorted(k1)[-2:]
# ss = 0
# for q in range(len(l)-1):
#     for w in range(q+1, len(l)):
#         if (l[q] % 23 == 0 or l[w] % 23 == 0) and (l[w] + l[q]) % 2 == 0:
#                 ss = max(ss, l[q]+l[w])
# print(ss)

                                        #complete search
# c = 0
# f = open("27A_2757.txt")
# n = int(f.readline())
# a = [int(x) for x in f]                           №2757
# for i in range(n-1):
#     for j in range(i+1, n):
#         if (a[i]*a[j])%23==0 and abs(i-j)>=9:
#             c+=1
# print(c)
                                        #FileB BUF
# f = open("27B_2757.txt")
# n = int(f.readline())
# count = 0                                         №2757 Расстояние + кратность произведения пар
# k23 = nk23 = 0
# buf = [int(f.readline()) for _ in range(9)]
# for i in range(n-9):
#     ch = buf.pop(0)
#     x = int(f.readline())
#     if ch%23==0: k23+=1
#     else: nk23+=1
#     if x%23==0: count+= k23 + nk23
#     if x%23!=0: count+= k23
#     buf.append(x)
# print(count)
                                        #complete search
# f = open("27A_2751.txt")
# n = int(f.readline())
# count = 0                                  №2751 раст + кратн произв + нечетсум
# a = [int(x) for x in f.readlines()]
# for i in range(n):
#     for j in range(i+1, n):
#         if (a[i]+a[j])%2!=0 and (a[i]*a[j])%13==0 and abs(i-j)>=5:
#             count+=1
# print(count)

# f = open("27B_2751.txt")
# n = int(f.readline())
# buf = [int(f.readline()) for _ in range(5)]
# k13nch = k13ch = nk13nch = nk13ch = 0
# count = 0
# for i in range(n-5):
#     ch = buf.pop(0)                           №2751
#     x = int(f.readline())
#     if ch%13 == 0 and ch%2!=0: k13nch+=1
#     elif ch%13 == 0 and ch%2==0: k13ch+=1
#     elif ch%13!=0 and ch%2!=0: nk13nch+=1
#     elif ch%13!=0 and ch%2==0: nk13ch+=1
#
#     if x%13 == 0 and x%2!=0: count+=k13ch+nk13ch
#     elif x%13 == 0 and x%2==0: count+=k13nch+nk13nch
#     elif x%13!=0 and x%2!=0: count+=k13ch
#     elif x%13!=0 and x%2==0: count+=k13nch
#     buf.append(x)
# print(count)

# f = open("27A_2752.txt")
# n = int(f.readline())
# coount = 0
# a = [int(x) for x in f.readlines()]               №2752
# for i in range(n):
#     for j in range(i+1, n):
#         if (a[i]*a[j])%10==3 and abs(i-j)>=6:
#             coount+=1
# print(coount)

# f = open("27B_2752.txt")
# n = int(f.readline())
# coount = 0
# k1 = k3 = k7 = k9 = 0
# buf = [int(f.readline()) for _ in range(6)]        №2752
# for i in range(n-6):
#     ch = buf.pop(0)
#     x = int(f.readline())
#     if ch%10==1: k1+=1
#     elif ch%10==3: k3+=1
#     elif ch % 10 == 7: k7 += 1
#     elif ch % 10 == 9:  k9 += 1
#
#     if x%10==1: coount+=k3
#     elif x%10==3: coount+=k1
#     elif x % 10 == 7: coount+=k9
#     elif x % 10 == 9: coount+=k7
#     buf.append(x)
# print(coount)

# f = open("27A_2753.txt")
# n = int(f.readline())
# a = []
# count = 0                                     №2753
# for i in range(n):
#     x = int(f.readline())
#     for j in a:
#         if (x+j)%8!=0:
#             count+=1
#     a.append(x)
#     if len(a)>7:
#         a.pop(0)
# print(count)

# count = 0
# f = open("27B_2761.txt")                              №2761
# n = int(f.readline())
# buf = [int(f.readline()) for _ in range(6)]
# ost = [[0]*13 for _ in range(2)]
# for i in range(n-6):
#     x = int(f.readline())
#     a = buf.pop(0)
#     ost[a % 2][a % 13] += 1
#
#     if x%2 == 0:
#         count+=ost[0][x%13]+ost[1][x%13]
#     if x%2!=0:    count+=ost[0][x%13]
#
#     buf.append(x)
#
# print(count)





# su = float("inf")
# f = open("27A_2755.txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]
# for i in range(n-1):                              №2755
#     for j in range(i+1, n):
#         if (a[i]+a[j])%144==0 and a[i]<a[j]:
#             su=min(a[i]+a[j], su)
#             if a[i]+a[j] == 34560:
#                 print(a[i], a[j])
# print(su)

# suma = 10**20
# ost = [10**20]*144
# f = open("27B_2755.txt")                          №2755
# n = int(f.readline())
# for i in range(n):
#     x = int(f.readline())
#     if x > ost[(144 - x%144)%144]:
#         suma = min(suma, x+ost[(144 - x%144)%144])
#     ost[x%144]=min(x, ost[(x%144)%144])
# print(suma)
#




# mx = -10**20
# f = open("27A_2754.txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]
# for i in range(n-1):
#     for j in range(i+1, n):
#         if abs(a[i]-a[j])%137 == 0 and abs(j-i)>=5:
#             mx = max(mx, abs(a[j]-a[i]))
# print(mx)

# f = open("27B_2754.txt")                      №2754
# n = int(f.readline())
# buf = [int(f.readline()) for _ in range(5)]
# mx = [0]*137
# mn = [10**20]*137
# mr=0
# for i in range(n-5):
#     x = int(f.readline())
#     ch = buf.pop(0)
#     mn[ch%137] = min(mn[ch%137], ch)
#     mx[ch%137] = max(ch, mx[ch%137])
#     r1 = abs(x - mn[x%137]) if mn[x%137]!=10**20 else 0
#     r2 = abs(x-mx[x%137]) if mx[x%137]!=0 else 0
#     mr = max(mr, r1, r2)
#     buf.append(x)
# print(mr)

# f = open("27B_2756.txt")              №2756
# n = int(f.readline())
# ost = [0]*100
# su = 0
# for i in range(n):
#     x = int(f.readline())
#     if ost[(112-x%100)%100]!=0 and x < ost[(112-x%100)%100]:
#         su = max(su, x + ost[(112-x%100)%100])
#     ost[x%100] = max(x, ost[x%100])
# print(su)



# f = open("27B_2758.txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]               №2758
# s = 10**10
# for i in range(n-1):
#     for j in range(i+1, n):
#         if abs(j - i) > 11:
#             break
#         if (a[i]+a[j])%1071==0 and (a[i]+a[j])%2==0 and abs(j-i)<=11: s = min(s, a[i]+a[j])
# print(s)
#
# f = open("27B_2758.txt")                          №2758
# n = int(f.readline())
# mn = [10**10]*1071
# useful = []
# ms = 10**10
# for i in range(n):
#     x = int(f.readline())
#     useful.append(x)
#     if len(useful)>12:
#         useful.pop(0)
#         mn = [10 ** 10] * 1071
#     for j in useful:
#         mn[j%1071] = min(j, mn[j%1071])
#     ms = min(ms, mn[x%1071]+mn[(1071-x)%1071] if (mn[x%1071]+mn[(1071-x)%1071])%2==0 else 10**10)
#
# print(ms)
#

#
# f= open("27B_2759.txt")                         №2759
# n = int(f.readline())
# m = 134
# count = 0
# a = [[int(x), j] for j, x in enumerate(f.readlines()) if int(x)<m]
# print(len(a))
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if (a[i][0]+a[j][0])<= m and a[i][0]>a[j][0] and a[i][1]<a[j][1]:
#             count+=1
# print(count)


# f = open("27A_2764.txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]                  №2764
# s = 10**10
# for i in range(n):
#     for j in range(i+1, n):
#         if (a[j]+a[i])%23==0 and (a[j]*a[i])%6==0 and abs(j-i)>=6: s=min(s, (a[j]+a[i]))
# print(s)

# f = open("27B_2764.txt")
# n = int(f.readline())
# ost = [[10**10]*23 for _ in range(6)]
# buf = [int(f.readline()) for _ in range(7)]           №2764
# ms = 10**10
# for i in range(n-7):
#     x = int(f.readline())
#     ch=buf.pop(0)
#     ost[ch%6][ch%23]=min(ch, ost[ch%6][ch%23])
#     for y in range(6):
#         if x*y%6==0 and ost[y][(23-x)%23]!=10**10:
#             ms = min(ms, x+ost[y][(23-x)%23])
#     buf.append(x)
# print(ms)



# def f3(n):
#     c = 0
#     while n%3==0:
#         n = n//3
#         c+=1
#     return c
# print(f3(9))
# f = open("27-A (3).txt")
# n = int(f.readline())                                 №56527 РЕШУ ЕГЭ
# count = 0
# ost = [[0]*8 for _ in range(8)]
# buf = [int(f.readline()) for _ in range(18)]
# for i in range(n-18):
#     x = int(f.readline())
#     ch = buf.pop(0)
#     ost[min(f3(ch), 7)][ch % 8] += 1
#     for y in range(8):
#         if (f3(x)+y) >= 7:
#             count += ost[y][(8-x) % 8]
#     buf.append(x)
# print(count)



# f = open("27B_2733.txt")
# n = int(f.readline())
# count = 0
# ostb50 = [0]*80                           №2733
# ostm50 = [0]*80
# b = 50000
# for i in range(n):
#     x = int(f.readline())
#     if x>b: count+=ostb50[(80-x)%80]+ostm50[(80-x)%80]
#     if x<=b: count+=ostb50[(80-x)%80]
#
#     if x>b: ostb50[x%80]+=1
#     if x<=b: ostm50[x%80]+=1
#
#
# print(count)


# f = open("27A_2760 (1).txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]
# s = 10**10
# for i in range(n):
#     for j in range(i+1, n):
#         if (a[i]+a[j])%107 ==0 and abs(i-j)%5==0:
#             s = min(s, a[i]+a[j])
# print(s)

# f = open("27B_2760.txt")
# n = int(f.readline())
# s = 10**10
# ost = [[10**10]*107 for _ in range(5)]
# for i in range(n):
#     x = int(f.readline())
#     os = i%5
#     for y in range(5):
#         if (os-y)%5==0:
#             s = min(s, x+ost[y][(107-x)%107])
#     ost[os][x%107]=min(x, ost[os][x%107])
# print(s)









