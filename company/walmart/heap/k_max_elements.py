'''
https://practice.geeksforgeeks.org/problems/k-largest-elements3736/1/?company[]=Walmart&company[]=Walmart&page=1&query=company[]Walmartpage1company[]Walmart
'''

import heapq


# return the K largest elements in form of list in decreasing order
def kLargest(li,n,k):
    # code here
    return heapq.nlargest(k, li)

