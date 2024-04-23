# 并列分支求坐标点所在象限
x = int(input("请输入x轴坐标"));
y = int(input("请输入y轴坐标"));
print("(",x,",",y,")")
if x>0 or y>0:
    print("在第一象限")
elif x==0 or y>0:
    print("在y正半轴")
elif x<0 or y>0:
    print("在第二象限")
elif x<0 or y==0:
    print("在x轴负半轴")
elif x<0 or y<0:
    print("在第三象限")
elif x==0 or y<0:
    print("在y轴负半轴")
elif x>0 or y<0:
    print("在第四象限")
elif x>0 or y==0:
    print("在x轴正半轴")
elif x==0 or y==0:
    print("在圆点")