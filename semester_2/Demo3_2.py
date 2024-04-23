numb = int(input("需要输入几个同学数据："))
a = 1
while numb>0:
    print("\n第",a,"个同学")
    list_name=["姓名","年龄","性别","学号","体重","身高"]
    姓名=input("请输入姓名:")
    年龄=int(input("请输入年龄:"))
    性别=input("请输入性别:")
    学号=input("请输入学号:")
    体重=float(input("请输入体重:"))
    身高=float(input("请输入身高:"))
    list_data=[姓名,年龄,性别,学号,体重,身高]
    for i in range(0,len(list_name)):
        print("%s:%s"%(list_name[i],list_data[i]))
    numb -= 1
    a += 1