class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here

  def traverse(root, arr):
    if root is None:
      return

    arr.append(root.val)

    if root.left is None and root.right is None:
      is_present = False
      if arr == sequence:
        is_present = True
      arr.pop()
      return is_present

    is_present = traverse(root.left, arr) or traverse(root.right, arr)
    arr.pop()
    return is_present

  return traverse(root, [])



def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
