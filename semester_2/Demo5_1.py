# 判断输入身份证号年月日，性别
id=input("请输入你的身份证号码：")
year=id[6:10]
month=id[10:12]
day=id[12:14]
age=id[16:17]
age=int(id[16:17])
print("出生为：",year,"年",month,"月",day,"日")
if age%2==0:
    print("女")
else:
    print("男")
# if id_city in list_id:
#     index=list_id.index(id_city)
#     print("您出身的城市是：",list_id.index(index+1))
# else:
#     print("没有")