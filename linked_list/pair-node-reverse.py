# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        def swapNode(head):
            if head is None or head.next is None:
                return            
            head.val, head.next.val = head.next.val, head.val
            swapNode(head.next.next)
            return head
        
        return swapNode(head)
            
            
        
