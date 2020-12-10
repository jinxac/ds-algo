"""
Write a function that moves the last element to the front in a given Singly Linked List.

For example, if the given Linked List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4.
"""

class Node():
  def __init__(self, val=0, nxt= None):
    self.val = val
    self.nxt = None


class LinkedList():
  def __init__(self):
    self.head = None
    self.last = None

  def append(self, val):
    if self.last is None:
      self.head = Node(val)
      self.last = self.head
    else:
      self.last.nxt = Node(val)
      self.last = self.last.nxt

class Solution():
  def solve(self, head):
    if not head:
      return None

    if not head.nxt:
      return head.val

    current = head
    prev = None
    while current.nxt != None:
      prev = current
      current = current.nxt

    new_node = Node(current.val)
    prev.nxt = None
    new_node.nxt = head

    return new_node


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  ll = LinkedList()
  for element in arr:
    ll.append(element)

  s = Solution()
  x = s.solve(ll.head)
  print(s.solve(ll.head))




