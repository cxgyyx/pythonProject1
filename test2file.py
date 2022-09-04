#while
# a = 10
# while a:    #0是一个界线，到0退出
#     print(a)
#     a -= 1
#
# a = -10
# while a:  # 0是一个界线，到0退出
#     print(a)
#     a += 1

#a = -10
#while a:  # 一直循环下去
#    print(a)
#    a -= 1

######################################
#for
# for i in 容器：   #可迭代对象 遍历
#     pass
# for i in range (10):
#     print (i)

# for i in range(1,5):
#     print(i)

# for i in range(5):
#     print(i+1)

# for i in range(1,6):
#     print(i)

# for i in range(1):
#     print(i)

# for i in range(0):
#     print(i)

# for i in range(-1):   #容器中不可能生成任何元素
#     print(i)
##########################
#if判断
#取偶数
# for i in range(10):
#     if i % 2 == 0:  #等于0为偶数
#      print(i)
#
# for i in range(10):
#     if not i % 2:  #先执行i%2 在执行not
#      print(i)


#取奇数
# for i in range(10):
#     if i % 2 == 1:  #等于1为奇数
#      print(i)

# for i in range(10):
#     if not i % 2 == 0:  #先执行i%2 在执行not
#      print(i)

#print(range(10))

# for i in range(10):
#     if not i & 1:  #and  & 位运算
#         print(i)
#
# for i in range(10):
#     if  i & 1:  #and  & 位运算
#         print(i)


# for i in range(1,10,2):  #1~10步长位2
#     print(i)
#
# for i in range(0,10,2):
#     print(i)

# for i in range(0,-2): #step=1 无法执行
#     print(i)
#
# for i in range(-10,1):
#     print(i)

for i in range(-2,3):
    if i:   #不包括0
        print(i)
