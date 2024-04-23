n = int(input("请输入班级人数"))
i = 1
while i<=n:
    name = input("请输入姓名")
    age = input("请输入年龄")
    h = input("请输入身高")
    print('核对以下信息')
    print('-'*40)
    print()
    print('姓名','年龄','身高',sep='   ')
    print()
    print(name,age,h,sep='   ',end="/信息核对完毕！")
    print()
    print()
    print('-'*40)
    i+=1