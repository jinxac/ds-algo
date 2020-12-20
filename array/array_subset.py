class Solution:
  def merge_method(self, arr1, arr2):
    arr1.sort()
    arr2.sort()

    start = 0

    while start < len(arr2):
      if arr1[start] != arr2[start]:
        return False
      start += 1

    return True

  def sort_binary_search(self, arr1, arr2):
    arr1.sort()

    def binary_search(arr, value):
      start = 0
      end = len(arr) - 1

      while start < end:
        mid = (start + end) // 2
        if arr[mid] == value:
          return True

        if arr[mid] < value:
          end = mid - 1
        else:
          start = mid + 1

      return False

    for i in range(len(arr2)):
      if not binary_search(arr1, arr2[i]):
        return False

    return True



  def is_subset(self, arr1, arr2):
    return self.merge_method(arr1, arr2)
