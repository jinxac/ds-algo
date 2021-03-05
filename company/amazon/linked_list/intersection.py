# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_length(self, head):
        length = 0
        
        while head:
            length += 1
            head = head.next
        
        return length
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        len_A = self.get_length(A)
        len_B = self.get_length(B)
        
        if not A or not B:
            return None
        
        p_A = A
        p_B = B
        
        diff = len_A - len_B
        if len_A > len_B:
            while diff > 0:
                p_A = p_A.next
                diff -= 1
        else:
            while diff < 0:
                p_B = p_B.next
                diff += 1
        
        while p_A and p_B:
            if p_A == p_B:
                return p_A
            
            p_A = p_A.next
            p_B = p_B.next
        
        return None
