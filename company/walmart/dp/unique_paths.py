'''
https://practice.geeksforgeeks.org/problems/number-of-unique-paths5339/1/?company[]=Walmart&company[]=Walmart&page=1&query=company[]Walmartpage1company[]Walmart
'''

'''
a = number of rows
b = number of columns
'''
def NumberOfPaths(a, b):
    #code here
    dp = []

    for i in range(a):
        dp.append([0] * b)

    for j in range(b):
        dp[0][j] = 1

    for i in range(a):
        dp[i][0] = 1

    for i in range(1, a):
        for j in range(1, b):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


    # print(dp)
    return dp[-1][-1]