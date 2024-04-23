# 元组
#问题解决
tuple = ("英语","思政","Python程序设置")
list1=[78,69,83]
list2=[89,87,76]
sum1=0
sum2=0
for i,j in zip(list1,list2):
    sum1+=i
    sum2+=j
# print("第一位学生，%s，%s，%s")
# 总成绩
print(sum1)
print(sum2)
print(list(zip(tuple,list1,list2)))