from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  # TODO: Write your code here
  if not root:
    return -1

  dq = deque()
  dq.append(root)

  # 12 7 1 9 10 5

  # 5 10
  while dq:
    element = dq.pop()
    if element.left:
      dq.appendleft(element.left)
    if element.right:
      dq.appendleft(element.right)

    if element.val == key:
      break

  return dq[-1] if dq else None




def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
