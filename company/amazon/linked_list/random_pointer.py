# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:    
    def copyRandomList(self, head):
        new_head = RandomListNode(-1)
        new_curr = new_head
        curr = head
        temp = {}
        
        while curr:
            node = RandomListNode(curr.label)
            temp[curr] = node
            new_curr.next = node
            new_curr = new_curr.next
            curr = curr.next
        
        curr = head
        
        while curr:
            random = curr.random
            if random:
                new_node = temp[curr]
                random_node = temp[random]
                new_node.random = random_node
            curr = curr.next
        
        return new_head.next
