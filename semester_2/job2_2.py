# 使用切片为列表增加元素
aList = [3,5,7]
print(aList[len(aList):])
# 在列表尾部增加元素
aList[len(aList):] = [9]
# 在列表头部插入多个元素
aList[:0] = [1,2]
# 在列表中间位置插入元素
aList[3:3] = [4]
print(aList)