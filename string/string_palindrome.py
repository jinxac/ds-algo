class Solution:
  def string_palindrome(self,s):
    start = 0
    end = len(s) - 1

    while start < end:
      if s[start] != s[end]:
        return False

      start += 1
      end -= 1

    return True



if __name__ == "__main__":
  s = input("")
  solution = Solution()
  print(solution.string_palindrome(s))