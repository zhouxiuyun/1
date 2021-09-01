#coding=gbk
import numpy as np
def edit_dis(str1, str2):
    m,n = len(str1),len(str2)

    dp=np.zeros((m+1, n+1), dtype=np.int64)

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
    return dp[m][n]



with open("input.txt","r") as file:
    str1 = file.readline()
    str2 = file.readline()
count = edit_dis(str1, str2)

file_writepath = 'output.txt'
file = open(file_writepath, "w")
file.write(str(count))

print(edit_dis(str1, str2))
