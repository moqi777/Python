# 打印三角形 正方形 长方形 平行四边形
for i in range(10):
    for j in range(0,10-i):
        print(end=" ")
    for k in range(10-i,10):
        print("*",end=" ")

    print("")

for i in range(10):
    for j in range(0,10-i):
        print(end="")
    for k in range(10-i,10):
        print("*",end="")

    print("")

for i in range(10):
    for j in range(0,10-i):
        print(end="")
    for k in range(10-i,10):
        print("*",end=" ")

    print("")

print("")
for i in range(10):
    for j in range(10):
        print("*",end="  ")
        
    print("")

print("")
for i in range(10):
    for j in range(5):
        print("*",end="  ")
        
    print("")

print("")
for i in range(6):
    for j in range(6-i,6):
        print(end=" ")
    for k in range(10):
        print("*",end="")
    print("")

# 输入一个正整数，输出该数的所有因子。（如6，其因子为6,3,2,1）（输入的正整数/i，若能整除，就是因子）
print("输入一个正整数，输出该数的所有因子。while循环实现")
sum = int(input("请输入正整数"))
i = sum
while True:
    if sum%i == 0:
        print(i)

    i -= 1

    if i == 0:
        break
print("输入一个正整数，输出该数的所有因子。for循环实现")
sum = int(input("请输入正整数"))
for i in range(sum,0,-1):
    if i==0:
        break
    if sum%i == 0:
        print(i)
# 输出所有的水仙花数（水仙花数是指一个3位数，它的每个位上的数字的3次幂之和等于它本身）
print("输出所有的水仙花数。while循环实现")
sum = 100
while sum<1000:
    a = int(sum/100)
    b = int(sum/10%10)
    c = sum%10
    if a*a*a + b*b*b + c*c*c == sum:
        print(sum)
    sum +=1
print("输出所有的水仙花数。for循环实现")
for i in range(100,1000):
    a = int(i/100)
    b = int(i/10%10)
    c = i%10
    if a*a*a + b*b*b + c*c*c == i:
        print(i)
# 实现整数的阶乘（n!=1*2*3*4...*n）
print("实现整数的阶乘。while循环水实现")
n = int(input("请输入正整数"))
i = 1
sum = 1
while i<n:
    sum += sum*i
    i += 1
print(sum)
print("实现整数的阶乘。for循环水实现")
n = int(input("请输入正整数"))
sum = 1
for i in range(1,n):
    sum += sum*i
    i += 1
print(sum)