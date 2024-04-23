#   编写程序，删除列表中所有素数
import random
list_num = []   #将十个一千以内的随机数储存在列表中
for x in range(10):
    list_num.append(random.randint(0,1000))
    x += x

print(list_num)

#创建一个数组用于存储非素数
not_numb = []
#遍历列表
for x in list_num:
    if x==1:
        not_numb.append(x)
        continue
    for i in range(2,x-1):
        #发现除了1和本身外仍有一个可以被自身整除的数，说明这个数不是素数
        if int(x/i)==(x/i):
            not_numb.append(x)#不是素数
            break
print(not_numb)