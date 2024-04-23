#   编写程序，要求输入一个字符串，然后将字符串中的所有字母全部后移一位，最后一个字母移到字符串的开头，最后输出新的字符串
str = input("请输入")
list = []
list.extend(str)
list.insert(0,list[len(list)-1])
list = list[0:len(list)-1]
print(''.join(list))