def longest_substring_with_k_distinct(str, k):
  temp = {}
  w_start = 0
  w_end = 0
  res = 0

  while w_end < len(str):
    if not str[w_end] in temp:
      temp[str[w_end]] = 0

    temp[str[w_end]] += 1

    while len(temp) > k:
      res = max(res, w_end - w_start)
      print("here...", temp)
      temp[str[w_start]] -= 1
      if temp[str[w_start]] == 0:
        del temp[str[w_start]]

      w_start += 1
    w_end += 1

    print("outside")

  print("----")
  return res


if __name__ == "__main__":
  s = "araaci"
  k = 2

  print(longest_substring_with_k_distinct(s, k))