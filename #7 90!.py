# f = open("24 (16).txt").readline()
# a = [i for i in range(len(f)) if f[i]=="A"]
# print(len(a))
# s = len(a)*(len(a)-1)//2
# print(s)
# cou = 0
# for k in range(len(f)-1):
#     if f[k]+f[k+1]=="AA":
#         cou+=1
# print(cou)
# print(s-cou)
# count = []
# f = open("9-210.txt").readlines()
# for i in range(len(f)):
#     a = [int(j) for j in f[i].split()]
#     print(a)
#     povt = [a.count(k) for k in a]
#     if sorted(a) == a or sum(povt)>5:
#         count.append(i+1)
# print(sum(count))
# print(f[3080].split())



# with open("26 (2).txt") as f:
#     n = f.readline()
#     m = [x.split() for x in f.readlines()]
#     m = sorted([[int(a), int(b)] for a, b in m])
#     m = [list(range(a, b+1)) for a, b in m]
# st = ""
# s = set()
# for i in m:
#     s = s|set(i)
# s = sorted(set(list(range(0, 1440)))-s)
#
# for j in range(1440):
#     if j in s:
#         st+="#"
#     else:
#         st+=" "
# print(len(s), len(st.split()))
#     m = [(-1, -1)] + sorted((int(a), int(b)) for a, b in m) + [(1440, 1440)]
#     print(m)
# l = []
# for i in range(len(m)-1):
#     if m[i][1] < m[i+1][0]:
#         l+=[(m[i+1][0]-1)- (m[i][1])]
#         if (m[i+1][0]-1)- (m[i][1])==5:
#             print(m[i], (m[i+1]))
# l = [k for k in l if k>1]
# print(l)
# print(sum(l), len(l))
# m = [list(range(x[0], x[1]+1))]
from random import *
# n = 1000
# k = 1
# cA = 0
# cB = 0
# lA = []
# a = [randint(1, 1000) for i in range(n)]
# a = [211, 103, 231, 786, 1, 247, 876, 183, 534, 54, 185, 458, 888, 844, 336, 164, 446, 716, 171, 238, 969, 528, 980, 166, 215, 191, 457, 440, 480, 70, 691, 974, 231, 812, 399, 823, 607, 253, 163, 642, 975, 713, 783, 118, 741, 511, 102, 537, 962, 486, 200, 475, 691, 175, 657, 656, 463, 942, 235, 535, 582, 877, 229, 229, 171, 424, 946, 577, 941, 218, 155, 308, 603, 896, 273, 556, 33, 912, 489, 38, 233, 267, 841, 634, 100, 375, 855, 735, 755, 471, 59, 775, 921, 785, 49, 167, 844, 226, 247, 148, 662, 721, 520, 422, 400, 67, 447, 47, 475, 66, 234, 299, 501, 222, 252, 835, 288, 33, 519, 750, 619, 286, 248, 362, 713, 781, 110, 470, 951, 523, 789, 152, 224, 653, 708, 763, 170, 852, 390, 159, 609, 184, 482, 460, 453, 901, 170, 808, 470, 317, 329, 820, 469, 878, 684, 963, 853, 634, 876, 782, 539, 476, 778, 923, 397, 288, 804, 459, 904, 572, 532, 58, 360, 705, 439, 198, 783, 624, 719, 197, 597, 229, 347, 356, 974, 608, 927, 616, 300, 70, 417, 200, 341, 175, 831, 446, 133, 91, 669, 728, 392, 554, 367, 633, 738, 417, 638, 260, 590, 663, 601, 649, 9, 242, 216, 96, 268, 105, 343, 934, 966, 223, 358, 877, 250, 85, 658, 569, 974, 345, 152, 954, 87, 117, 950, 535, 526, 254, 197, 987, 556, 473, 846, 613, 65, 605, 221, 184, 629, 872, 842, 463, 131, 802, 349, 418, 533, 735, 679, 708, 679, 994, 359, 821, 422, 405, 425, 321, 518, 224, 1, 926, 202, 476, 21, 452, 210, 288, 495, 38, 357, 242, 336, 747, 854, 610, 526, 488, 539, 24, 619, 303, 518, 202, 313, 522, 461, 170, 205, 599, 23, 392, 900, 798, 873, 800, 588, 959, 107, 625, 388, 322, 997, 345, 442, 831, 237, 912, 330, 389, 281, 961, 787, 750, 608, 939, 719, 646, 966, 864, 58, 187, 231, 672, 156, 89, 251, 87, 465, 716, 45, 62, 886, 650, 793, 610, 969, 89, 130, 948, 764, 364, 138, 270, 191, 344, 559, 665, 981, 813, 108, 449, 454, 666, 411, 663, 566, 122, 862, 838, 21, 395, 120, 610, 612, 596, 646, 193, 565, 32, 946, 285, 384, 83, 885, 233, 769, 939, 781, 435, 848, 585, 2, 616, 109, 906, 383, 384, 778, 599, 873, 546, 180, 750, 742, 464, 216, 733, 856, 306, 39, 116, 182, 618, 1, 117, 744, 394, 507, 468, 521, 973, 798, 997, 359, 553, 376, 409, 720, 611, 696, 968, 18, 435, 813, 480, 490, 600, 924, 341, 854, 621, 261, 610, 626, 329, 910, 858, 330, 273, 700, 528, 717, 226, 183, 245, 317, 318, 275, 501, 527, 295, 339, 624, 828, 281, 645, 737, 980, 519, 911, 108, 129, 22, 76, 789, 110, 48, 333, 407, 432, 900, 561, 882, 653, 733, 713, 73, 261, 827, 620, 430, 130, 373, 824, 630, 190, 167, 515, 813, 910, 456, 921, 900, 861, 741, 184, 442, 592, 439, 718, 911, 818, 723, 913, 642, 633, 4, 188, 772, 424, 542, 409, 266, 457, 59, 958, 502, 990, 55, 204, 6, 776, 44, 315, 426, 155, 808, 872, 283, 968, 414, 695, 51, 141, 619, 82, 866, 626, 227, 550, 664, 102, 249, 81, 906, 371, 718, 458, 974, 733, 347, 636, 577, 993, 754, 370, 219, 947, 217, 859, 212, 832, 675, 281, 165, 573, 18, 388, 588, 502, 302, 938, 345, 39, 726, 386, 586, 89, 55, 600, 930, 648, 416, 245, 440, 866, 179, 933, 124, 828, 956, 236, 286, 542, 576, 356, 335, 743, 836, 664, 909, 196, 662, 695, 339, 197, 172, 619, 746, 245, 797, 403, 355, 404, 311, 619, 710, 370, 867, 196, 130, 644, 930, 561, 191, 107, 227, 176, 890, 238, 107, 91, 988, 112, 98, 294, 876, 297, 603, 943, 574, 353, 632, 34, 898, 389, 4, 769, 397, 8, 826, 22, 2, 923, 412, 703, 345, 246, 888, 793, 766, 914, 572, 400, 842, 38, 563, 939, 902, 834, 635, 576, 454, 41, 214, 620, 919, 940, 446, 375, 693, 203, 249, 402, 672, 797, 281, 53, 760, 524, 814, 508, 384, 165, 963, 763, 246, 686, 259, 185, 452, 222, 602, 125, 324, 424, 516, 200, 960, 865, 280, 529, 948, 336, 540, 589, 160, 240, 219, 924, 834, 573, 842, 616, 424, 838, 109, 837, 607, 392, 471, 923, 792, 430, 325, 397, 175, 279, 114, 544, 457, 776, 163, 978, 387, 402, 798, 975, 911, 595, 691, 390, 573, 897, 803, 677, 320, 79, 527, 769, 77, 219, 835, 781, 91, 522, 554, 722, 263, 523, 92, 816, 198, 303, 493, 678, 856, 535, 504, 752, 826, 986, 487, 83, 317, 800, 747, 339, 131, 474, 743, 197, 393, 292, 164, 957, 379, 361, 993, 47, 937, 39, 640, 482, 22, 151, 241, 966, 700, 981, 267, 400, 191, 183, 243, 186, 61, 496, 447, 706, 991, 11, 500, 300, 478, 216, 793, 20, 120, 622, 230, 494, 148, 610, 337, 390, 492, 793, 904, 755, 486, 316, 771, 442, 849, 663, 484, 171, 243, 30, 743, 167, 39, 18, 411, 910, 409, 652, 173, 75, 905, 18, 602, 781, 255, 759, 260, 959, 674, 341, 419, 646, 177, 192, 966, 647, 126, 812, 18, 54, 271, 230, 160, 815, 659, 987, 213, 871, 776, 73, 655, 207, 523, 605, 849, 902, 67, 727, 893, 787, 794, 533, 323, 514, 105, 557, 548, 532, 637, 913, 883, 719, 800, 571, 478, 589, 961, 65, 692, 206, 348, 508, 428, 396, 991, 882, 960, 653, 680, 828, 409, 183, 104, 863, 137, 661, 856, 14, 28, 302, 258, 15, 266, 760, 422, 950, 132, 503, 938, 480, 640, 747, 37, 969, 830, 950, 669, 731, 882, 641, 844, 64, 331, 830, 230, 677, 91, 596, 812, 502, 762, 511, 208, 665, 559, 685, 849, 595, 115, 515, 484, 672, 558, 983, 219, 18, 390, 823, 950]
# a = [int(x) for x in open("27990_B.txt").readlines()]
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if abs(a[i]-a[j])%2==0 and (a[i]%17==0 or a[j]%17==0):
#             lA+=[[a[i], a[j]]]
# print([x for x in lA if sum(x)==max([sum(t) for t in lA])])
#         if (a[i]*a[j])%62==0:
#             cA+=1
# print(cA)
# p1 = 0
# p2 = 0
# kk = k2 = k31 = k62 = 0
#
# for x in range(len(a)):
#     if a[x]%62==0: cB+=kk
#     elif a[x]%31==0: cB+=k2
#     elif a[x]%2==0: cB+=k31
#     else: cB+=k62
#     kk+=1
#
#     if a[x]%62==0: k62+=1
#     if a[x]%31==0: k31+=1
#     if a[x] % 2 == 0: k2+=1
# print(cA)
# print(cB)
# print(p1, p2)
#
# def n3(n):
#     k = 0
#     while n%3==0:
#         k+=1
#         n//=3
#     return k
# count = 0
# f = open("27-B (1).txt")
# n = int(f.readline())
# ost = [[0]*8 for _ in range(8)]
# buf = [int(f.readline()) for i in range(18)]
# for i in range(n-18):
#     y = buf.pop(0)
#     ost[min(n3(y), 7)][y%8]+=1
#     x = int(f.readline())
#     tx = n3(x)
#     for d in range(8):
#         if tx+d>=7:
#             count+=ost[d][(8-x%8)%8]
#
#     buf += [x]
# print(count)
# def f(n):
#     l = [i for i in range(2,n) if n%i==0]
#     return l
# print(f(62))
# print(4*13)
# print(3*18)
# count = 0
# k = 200
# n = 1000
# a = [randint(1, 1000) for i in range(n)]
# k41 = [0]*120
# kn41 = [0]*120
# for i in range(k, n):
#     if a[i-k]%41==0:
#         ost = a[i-k]%120
#         k41[ost]+=1
#     else:
#         ost = a[i - k] % 120
#         kn41[ost] += 1
#     if a[i]%41:
#         ost2=0 if a[i]%120==0 else 120-a[i]%120
#         count+=kn41[ost2]
#     else:
#         ost2 = 0 if a[i] % 120 == 0 else 120 - a[i] % 120
#         count += k41[ost2]
# print(count)


# f = open("28131_A.txt").readlines()
# k = 84240
# a = sorted([int(x) for x in f], reverse=True)
# print(a)
# for x in range(1, len(a)-1):
#     for y in range(x+1, len(a)):
#         if a[x]+a[y]==k:
#             print(a[x], a[y])
#             break


