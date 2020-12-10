# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
 This problem has few corner cases which need to be taken care of :-
 
 1. If all the elements are deleted and list becomes empty. For example, list is [6,6,6,6] and element to be deleted is 6. 
 2. If first element is same the target element. Since in our solution we are iterating using nxt element, so first element
    is always left. So need to handle that. For example, in this case [5,3,2,1,5,5,5,5], we return head.next
 3. If elements are consecutive then we iterate till the last occurence and then assign the curr pointer to next of nxt.
    For example, [3,4,5,5,5,5,5,1,2].
'''

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        curr = head
        while curr is not None:
            nxt = curr.next
            if nxt and val == nxt.val:
                while nxt is not None and val == nxt.val:
                    nxt = nxt.next
                curr.next = nxt
            curr = nxt
        
        if head.val == val:
            return head.next
        
        return head
