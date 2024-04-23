# S2354 郑伊龙
a = int(input("请输入第一个整数"))
b = int(input("请输入第二个整数"))
if a<b :
    print("a：",a,"b：",b)
else:
    a,b = b,a
    print("a：",a,"b：",b)