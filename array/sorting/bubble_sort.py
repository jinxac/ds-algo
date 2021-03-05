def bubble_sort(arr):
  end = len(arr)
  isSorted = False

  while end > 0:
    isSorted = True
    for j in range(0, end - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        isSorted = False

    if isSorted:
      break

    end -= 1

  print(arr)


if __name__ == "__main__":
  arr = [5,3,3,5,1]
  bubble_sort(arr)
