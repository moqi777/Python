aList = [3,5,7]
aList[len(aList):]
print(aList[len(aList):])

aList[len(aList):] = [9]    
aList[:0] = [1,2]
aList[3:3] = [4]
aList
print(aList)