'''
https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1/?company[]=Walmart&company[]=Walmart&page=1&query=company[]Walmartpage1company[]Walmart
'''

def toSumTree(root) :
    if root is None:
        return 0

    if root.left is None and root.right is None:
        temp = root.data
        root.data = 0
        return temp


    sub_sum = toSumTree(root.left) + toSumTree(root.right)
    temp = root.data
    root.data = sub_sum

    return sub_sum + temp