# 1.计算1-100（含）之间所有奇数/偶数的和
# while
print("-"*40)
print("计算1-100（含）之间所有奇数/偶数的和while循环结果")
a = 0   #奇数
b = 0   #偶数
i = 1
while i<=100:
    if i%2 == 0:
        b += i
    else:
        a += i
    i+=1
print("1-100的所有奇数合为",a)
print("1-100的所有偶数合为",b)
# for
print("-"*40)
print("计算1-100（含）之间所有奇数/偶数的和for循环结果")
a = 0   #奇数
b = 0   #偶数
for i in range(1,101):
    if i%2 == 0:
        b += i
    else:
        a += i
print("1-100的所有奇数合为",a)
print("1-100的所有偶数合为",b)

# 2.求1-n的和，n为任意正整数
# while
print("-"*40)
print("求1-n的和，n为任意正整数while循环结果")
n = int(input("请输入n的值"))
i = 1
sum = 0
while i<=n:
    sum += i
    i += 1
print("1 -",n,"的和为",sum)
# for
print("-"*40)
print("求1-n的和，n为任意正整数for循环结果")
n = int(input("请输入n的值"))
sum = 0
for i in range(1,n+1):
    sum += i
print("1 -",n,"的和为",sum)

# 3.输入n名学生的成绩，求所有成绩的平均值
# while
print("-"*40)
print("输入n名学生的成绩，求所有成绩的平均值while循环结果")
n = int(input("请输入有几名学生"))
sum = 0
i = 1
while i<=n:
    num = "请输入第",i,"名学生的成绩"
    score = int(input(num))                                                                                                                                
    sum += score
    i += 1
print("所有成绩的平均值为",sum/n)
# for
print("-"*40)
print("输入n名学生的成绩，求所有成绩的平均值for循环结果")
n = int(input("请输入有几名学生"))
sum = 0
for i in range(1,n+1):
    num = "请输入第",i,"名学生的成绩"
    score = int(input(num))                                                                                                                                
    sum += score
print("所有成绩的平均值为",sum/n)

# 4.求1-50之间所有奇数的乘积
# while
print("-"*40)
print("求1-50之间所有奇数的乘积while循环结果")
sum =1
i = 1
while i<=50:
    if i%2 ==1:
        sum *= i
    i += 1
print("1-50之间所有的奇数乘积为：",sum)
# for
print("-"*40)
print("求1-50之间所有奇数的乘积for循环结果")
sum = 1
for i in range(1,51):
    if i%2 ==1:
        sum *= i
print("1-50之间所有的奇数乘积为：",sum)

# 5.输出1-300之间，所有能被7和4整除的数
# while
print("-"*40)
print("输出1-300之间，所有能被7和4整除的数while循环结果")
i = 1
while i<=300:
    if i%7 == 0:
        print(i)
    elif i%4==0:
        print(i)
    i += 1
# for
print("-"*40)
print("输出1-300之间，所有能被7和4整除的数for循环结果")
for i in range(1,301):
    if i%7 == 0:
        print(i)
    elif i%4==0:
        print(i)

# 6.输入n个正整数，找出其中的奇数并输出
# while
print("-"*40)
print("输入n个正整数，找出其中的奇数并输出while循环结果")
n = int(input("您想要输入几个数："))
i = 0
sum = []
while i<n:
    sum.append(int(input("请输入正整数：")))
    i += 1
i = 0
print("奇数有：")
while i<n:
    if sum[i]%2 == 1:
        print(sum[i])
    i += 1
# for
print("-"*40)
print("输入n个正整数，找出其中的奇数并输出for循环结果")
n = int(input("您想要输入几个数："))
sum = []
for i in range(n):
    sum.append(int(input("请输入正整数：")))
print("奇数有：")
for i in range(n):
        if sum[i]%2 == 1:
            print(sum[i])