"""
Weak Sections:-

1. BackTracking
2. Greedy
3. DP
4. Graphs
5. Heaps
6. Bitwise
7. 2 pointer boundary conditions / simple code


Weak Problem type:-

1. Palindromes
2. Subsets
3. Partioning
4. Linked list recurse reverse
5. Postorder iterative traversal for tree
6. heapq implemenation for nlargest etc..
7. 2 Trees (Merge)



Problems to check:-

1. Balanced tree iterative(https://leetcode.com/problems/balanced-binary-tree/)
2. Greater sum tree iterative(https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1/?company[]=Walmart&company[]=Walmart&page=1&query=company[]Walmartpage1company[]Walmart)
3. Special stack
4. Maximum sum rectangle
5.Check for formula -> https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
6. sieve of eratosthenes
7. GCD Algorithm
8. min height of binary tree
9. linked list cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        slow = A
        fast = A.next

        while fast !=None and fast.next!=None and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if fast is None:
            return None

        slow = A

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
 10. tree merge -> https://www.interviewbit.com/problems/merge-two-binary-tree/
 11. repeat again -> https://www.interviewbit.com/problems/remove-consecutive-characters/
 12. Three sum -> https://www.interviewbit.com/problems/3-sum-zero/
 13. Duplicates, Duplicates 2, Remove element (Check solutions on leetcode)
 14. Bitwise trailing zeros using lookup table
 15. Rotate image
 16. Check for alternate solution -> https://www.interviewbit.com/problems/sort-binary-linked-list/
 17. Checkout the solution -> https://www.interviewbit.com/problems/numrange/
 18. Check division float conversion -> https://www.interviewbit.com/problems/evaluate-expression/
 19. Check in place -> https://leetcode.com/problems/odd-even-linked-list/
 20. Check for stack approach -> https://www.interviewbit.com/problems/maximum-unsorted-subarray/
"""