while True :
    name = input("请输入姓名：") 
    age = input("请输入性别：")
    time = input("请输入出生年月：")
    relathon = input("请输入联系方式：")
    print('核对以下信息')
    print('-'*40)
    print()
    print('姓名','性别','出生年月','联系方式',sep='   ')
    print()
    print(name,age,time,relathon,sep='   ',end='/信息核对完毕!')
    print()
    print('-'*40)
    sum = input('是否继续输入：')
    print()
    if sum == '否' :
        break

