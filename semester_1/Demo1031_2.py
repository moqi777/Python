# S2354 郑伊龙
a = int(input("请输入第1个整数："))
b = int(input("请输入第2个整数："))
print("输入值：",a,",",b)
if a<b :
    a,b = b,a
print("降序值：",a,",",b)