# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        hasCycle = False

        if not head:
            return None

        while fast!=None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                hasCycle = True
                break

        if not hasCycle:
            return None

        slow = head

        while True:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next


