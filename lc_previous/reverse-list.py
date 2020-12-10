# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseListIterative(self, head):
        prev = None
        curr = head
        
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def reverseListRecursive(self, head):        
        def reverse(curr, prev):
            if curr is None:
                return prev
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            return reverse(nxt, prev)
        
        return reverse(head, None)
    
    def reverseList(self, head: ListNode) -> ListNode:
        # return self.reverseListIterative(head)
        return self.reverseListRecursive(head)
