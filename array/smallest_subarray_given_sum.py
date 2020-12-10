def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  start = 0
  end = 0
  curr_sum = 0
  res = len(arr)

  while end < len(arr):
    curr_sum += arr[end]
    while curr_sum >= s:
      res = min(res, end - start + 1)
      curr_sum -= arr[start]
      start += 1
    end += 1

  return res
