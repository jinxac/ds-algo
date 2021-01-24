'''
https://practice.geeksforgeeks.org/problems/mirror-tree/1/?company[]=Walmart&company[]=Walmart&page=1&query=company[]Walmartpage1company[]Walmart
'''


'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
def mirror(root):
    # Code here
    if root is None:
        return

    mirror(root.left)
    mirror(root.right)

    root.left, root.right = root.right, root.left
    return root