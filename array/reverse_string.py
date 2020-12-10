def convert_string(string):
    i = 0
    temp = ""
    while i < len(string):
        j = i + 1
        while j < len(string) and string[i] != string[j]:
            j += 1

        temp += (j-i) + string[i]
        j = i

    return temp

class Solution:
  def reverse_string(self,s):
    res = ""
    for i in s:
      res = i + res

    return res

  def reverse_string_slice(self, s):
    return s[::-1]

  def reverse_string_recursion(self, s):
    # implement this
    return None

  def reverse_string_reversed(self, s):
    return ''.join(reversed(s))



if __name__ == "__main__":
  s = input("Enter name")
  solution = Solution()
  print(solution.reverse_string(s))
  print(solution.reverse_string_slice(s))
  print(solution.reverse_string_reversed(s))