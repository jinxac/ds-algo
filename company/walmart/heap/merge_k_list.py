from heapq import *

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __lt__(self, other):
    return self.val < other.val


class Solution:
  def solve(self, lists):
    min_heap = []

    for root in lists:
      if root:
        heapq.heappush(min_heap, root)

    head, tail = None, None

    while min_heap:
      node = heappop(min_heap)

      if node is None:
        head = tail = node
      else:
        tail.next = node
        tail = tail.next

      if node.next:
        heapq.heapush(min_heap, node.next)

    return head
