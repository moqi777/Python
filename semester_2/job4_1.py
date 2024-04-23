# 已知list_a=[1,2,3,4,5,6]，请通过两种方法实现，使list_a=[6,5,4,3,2,1]

# 方法一
list_a=[1,2,3,4,5,6]
list_a.reverse()# 倒序输出
print(list_a)

# 方法二
list_a=[1,2,3,4,5,6]
list_a.sort(reverse=True)   #从高到低输出
print(list_a)