def selection_sort(arr):
  if not arr:
    return None

  start = 0

  while start < len(arr) - 1:
    min_element = float('inf')
    min_index = 0

    for j in range(start+1, len(arr)):
      if min_element > arr[j]:
        min_index = j
        min_element = arr[j]

    if min_element < arr[start]:
      arr[start], arr[min_index] = arr[min_index], arr[start]

    start += 1

  print(arr)


if __name__ == "__main__":
  arr = [1,5,3,2,4]
  selection_sort(arr)