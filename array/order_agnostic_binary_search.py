def binary_search(arr, key):
  # TODO: Write your code here
  start = 0
  end = len(arr) - 1
  is_descending = arr[start] > arr[end]

  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
      return mid

    if arr[mid] > key:
      if is_descending:
        start = mid + 1
      else:
        end = mid - 1
    else:
      if is_descending:
        end = mid - 1
      else:
        start = mid + 1
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()
