#fd(k*n)-вперед k-колво пикс n-увеличение воскок
#rt- вправо
#lt- влево

# from turtle import *
# tracer(0)
# r = 25
# screensize(-10000, 10000)
# for i in range(7): #сколько раз повторяется
#    rt(90)
#    fd(4*r)
#    for j in range(2):
#       lt(90)
#       fd(4*r)
# up()
# for x in range(-20, 20):
#    for y in range(-20, 20):
#       goto(x*r, y*r)
#       dot(3, "green")
# update()
# done()


# from turtle import *
# tracer(0)
# r = 20
# screensize(10000, 10000)
# for i in range(7):
#    goto(xcor()+6*r,ycor()-9*r)
#    goto(xcor() -6 * r, ycor() +2 * r)
#    goto(xcor() + 12 * r, ycor() + 3 * r)
# up()
# for x in range(-20, 20):
#    for y in range(-20, 20):
#       goto(x*r, y*r)
#       dot(3, "green")
# update()
# done()






from itertools import *
nch = "135"
c = 0
for i in product("01234567", repeat=5):
   i = "".join(i)
   print(i)
   if i[0]!="0" and i.count("7")==3:
      s = i
      print(s)
      for j in nch:
         s = s.replace(f"{j}", "*")
      if "77" not in s and "*7" not in s and "7*" not in s:
         c+=1
print(c)



#
# from turtle import *
# tracer(0)
# r = 25
# for i in range(3):
#     fd(7*r)
#     rt(90)
# fd(8*r)
# for j in range(3):
#     lt(90)
#     fd(5*r)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*r, y*r)
#         dot(3, "green")
# done()

from turtle import *
# screensize(10000, 10000)
# tracer(0)
# r = 25
# rt(45)
# for i in range(7):
#     fd(5*r)
#     rt(45)
#     fd(10*r)
#     rt(135)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*r, y*r)
#         dot(3, "green")
# update()
# done()


#
# screensize(1000, 1000)
# tracer(0)
# r = 25
# for i in range(9):
#     fd(18*r)
#     rt(72)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*r, y*r)
#         dot(3, "green")
# update()
# done()




