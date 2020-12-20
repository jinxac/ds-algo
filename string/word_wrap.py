class Solution:
    def solve(self, arr, characters_allowed):
        if not arr:
            return []

        if len(arr) == 1:
            if arr[0] <= characters_allowed:
                return [1,1]
            return []

        result = []
        curr = 0

        while curr < len(arr):
            nxt = curr + 1
            if curr == len(arr) - 1:
                result.append(curr + 1)
                result.append(curr + 1)
                break

            temp_sum = arr[curr] + arr[nxt] + 2
            while nxt < len(arr) and  temp_sum <= characters_allowed:
              temp_sum = temp_sum + arr[nxt] + 1
              nxt += 1

            result.append(curr + 1)
            result.append(nxt)

            curr = nxt

        print(result)


s = Solution()
s.solve([3,2,2], 4)