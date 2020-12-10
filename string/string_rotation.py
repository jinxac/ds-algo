'''

Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
'''

class Solution:

  def string_rotation_use_twice(self, s1, s2):
    if len(s1)!= len(s2):
      return False

    temp = s1 * 2;

    return temp.count(s2) > 0

  def string_rotation(self,s1, s2):
    start_element = s1[0]

    current = 0

    while current < len(s2) and start_element != s2[current]:
      current += 1

    temp_str = s2[current:] + s2[0:current]

    print("here", temp_str)

    return s1 == temp_str




if __name__ == "__main__":
  s1 = input("")
  s2 = input("")
  solution = Solution()
  print(solution.string_rotation(s1, s2))

