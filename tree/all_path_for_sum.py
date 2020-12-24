class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  # TODO: Write your code here
  def traverse(root, curr_sum, arr):
    if root is None:
      return

    if root.left is None and root.right is None:
      if root.val + curr_sum == sum:
        arr.append(root.val)
        allPaths.append(arr)
    else:
      arr.append(root.val)
      traverse(root.left, curr_sum + root.val, arr)
      traverse(root.right, curr_sum + root.val, arr)

    arr.pop()

  traverse(root, 0, [])

  print("here", allPaths)


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
