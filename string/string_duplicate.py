class Solution:
  def string_duplicate(self,s):
    for element in s:
      if element in temp:
        temp[element] += 1
      else:
        temp[element] = 1

    for key, value in temp.items():
      if value > 1:
        print(key)



if __name__ == "__main__":
  s = input("")
  solution = Solution()
  print(solution.string_duplicate(s))