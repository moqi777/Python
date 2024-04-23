# 嵌套分支求三个数降序
# 1 2 3	a<b<c	a,c = c,a
# 1 3 2	a<c<b	a,b,c = b,c,a
# 3 2 1 	
# 3 1 2 b<c<a	b,c = c,b
# 2 1 3	b<a<c	a,b,c = c,a,b
# 2 3 1	c<a<b	a,b,c = b,a,c
a = int(input("请输入第一个数"));
b = int(input("请输入第二个数"));
c = int(input("请输入第三个数"));
if a<b:
    if b<c:
        a,c = c,a
    elif b>c:
        if a>c:
            a,b,c = b,a,c
        elif a<c:
            a,b,c = b,c,a
elif b<a:
    if c<a:
        b,c = c,b
    elif a<c:
        a,b,c = c,a,b

print(a,b,c)
    