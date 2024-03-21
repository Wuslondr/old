#ШАСТИН ВАРИАНТ 4 МОЙ СПОСОБ
# with open("24 (22).txt") as f:
#     st = f.readline()
#     ind = [i for i in range(len(st)-1) if st[i] > st[i+1]]
#     ind1 = max([abs(ind[i] - ind[i+100001]) for i in range(len(ind)-100001)])
# print(ind1)

#Метод двух указателей
# with open("24 (24).txt", encoding="utf-8") as f:
#     s = f.readline().rstrip()
# l = 0
# ky = 0
# m = 0
# for r in range(len(s)):
#     if s[r]=="Y": ky+=1
#     while ky>100:
#         if s[l]=="Y": ky-=1
#         l+=1
#     m = max(m, r-l+1)
# print(m)

# with open('24 (25).txt', encoding='utf-8') as f:
#     s = f.readline().rstrip()
#
# l = 0
# k = 0
# m = 10**6
# for r in range(len(s)):
#     if s[r]=="T": k+=1
#     while k>=100:
#         if s[l]=="T": k-=1
#         l+=1
#         if k==100: m = min(m, r-l+1)
# print(m)
# with open("24 (22).txt", encoding="utf-8") as f:
#     s = f.readline().rstrip()
#
# l = 0
# k = 0
# m = 0
#
# for r in range(1, len(s)):
#     if s[r-1] > s[r]: k+=1
#     while k > 100000:
#         if s[l] > s[l+1]: k-=1
#         l+=1
#     if k == 100000: m = max(m, r-l+1)
# print(m)


# f = open("107_24.txt").readline().replace("AB", "X").replace("CB", "X")
# cmax = 0
# for i in range(len(f)):
#     if f[i]=="X":
#         c+=1
#
#     else:
#         cmax = max(c, cmax)
#         c=0
# print(cmax)
#



# f = open("modify.txt").readline()
# # l = 0
# c = 0
# m = 0
# nch = "13579"
# for i in nch:
#     f = f.replace(f"{i}", "*")
# for j in range(0, len(f)-2):
#     if f[j+2]=="*" and f[j+1]=="*" and f[j]=="*":   NOOB
#         m = max(c, m)
#         c = 2
#     else: c+=1



# for r in range(2, len(f)):
#     if f[r] in nch and f[r-1] in nch and f[r-2] in nch: c += 1
#     while c >= 1:
#         if f[l] in nch and f[l+1] in nch and f[l+2] in nch: c -= 1  PRO
#         l+=1
#     if c==0: cmax = max(r-l+1, m)





