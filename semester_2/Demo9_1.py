
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