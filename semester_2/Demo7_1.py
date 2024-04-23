# 求一个3×3矩阵的两条对角线元素之和（注意：两条对角线交叉点处的元素只计算一次）
x = [[17,7,3],[4,5,6],[7,8,9]]
sum = 0
for i in range(len(x)):
    for j in range(len(x[i])):
        if i%2 == 0:    # x轴为偶数时
            if j%2 == 0:
                sum += x[i][j]
        else:
            if j%2 == 1:
                sum += x[i][j]
print(sum)
