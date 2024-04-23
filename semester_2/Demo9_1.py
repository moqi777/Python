# 字典的五种创建方法
stu_info1 = {'num':'20180101','name':'Liming','sex':'male'}
# 直接赋值创建字典
stu_info2 = dict(stu_info1)
# 通过其他字典创建
stu_info3 = dict((['num','20180101'],['name','Liming'],['sex','male']))
# 通过“（键，值）”对的序列创建
stu_info4 = dict(num = '20180101',name = "Liming",sex = "male")
# 通过关键字参数创建
stu_info5 = dict(zip(['num','name','sex'],['20180101','Liming','male']))
# 通过idct和zip结合创建

# 元组
tuplel = ("学号","姓名","性别","出生年月")
# 列表
list1 = ["2023001","张三","男","2005年4月"]
list2 = ["2023002","李四","女","2006年6月"]
list3 = ["2023003","王五","男","2007年7月"]

# 列表
x=list(zip(tuplel,list1))
print(x)
# 字典
dict1=dict(zip(tuplel,list1))
print(dict1)
# 元组
tuple2 = tuple(zip(tuplel,list1))
print(tuple2)

# 字典的创建
dict2 = {"学号":"2023001","姓名":"张三"}
print(dict2)
dict3 = {'学号':'2023002','姓名':'李四'}
print(dict3)

keys = ['a','b','c']
values = (1,2,3)
d4 = dict(zip(keys,values))
print(d4)

d5 = dict(学号='2023001',姓名='张三',性别='男')
print(d5)
