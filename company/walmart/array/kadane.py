'''
https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1/?company[]=Walmart&company[]=Walmart&page=1&query=company[]Walmartpage1company[]Walmart
'''

def maxSubArraySum(a,size):
    ##Your code here
    curr_sum = 0
    max_sum = 0

    for i in range(size):
        curr_sum = max(a[i], curr_sum + a[i])
        max_sum = max(curr_sum, max_sum)

    return max_sum