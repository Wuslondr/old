f = open("modify.txt").readlines()
cn = 0
# for i in f:
#     st = [int(x) for x in [a for a in i.split()]]
#     povt = [x for x in st if st.count(x)>1]
#     nepovt = [x for x in st if st.count(x)==1]
#     if len(povt)>0 and len(nepovt)>0:
#         if (sum(nepovt)/len(nepovt))>(sum(povt)/len(povt)):
#             c+=1
# print(c)

# a = [[int(x) for x in s.split()] for s in f]
# b = [[a[i][j] for i in range(len(a))] for j in range(6)]
# for i in range(len(a)):
#     k = 0
#     for y in range(6):
#         if a[i].count(b[y][i])==1 and b[y].count(b[y][i])>150:
#             k+=1
#     if k>=5:
#         c+=1
# print(c)

# for i in f:
#     a, b, c = sorted([int(x) for x in i.split()])
#     gr1 = a*b
#     gr2 = a*c
#     gr3 = b*c
#     if (gr1+gr2)>gr3: cn+=1
# print(cn)





