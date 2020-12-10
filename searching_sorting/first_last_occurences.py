#code
class Solution:
    def solve(self, arr, target):
        start = 0
        end = len(arr) - 1
        s_i = -1
        l_i = -1

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                if arr[mid - 1] == target and not arr[mid+1] == target:
                    l_i = mid
                    end = mid - 1

                if not arr[mid - 1] == target and arr[mid+1] == target:
                    s_i = mid
                    start = mid + 1

                else:
                    temp = mid
                    while temp > 0 and arr[temp] == arr[temp - 1]:
                        temp -= 1

                    s_i = temp

                    temp = mid

                    while temp < len(arr) and arr[temp] == arr[temp + 1]:
                        temp += 1

                    l_i = temp

                return str(s_i) + " " + str(l_i)

            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1




if __name__ == "__main__":
    t = int(input())
    while t:
        n, x = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        print("here...", n, x, arr)
        solution = Solution()
        print(solution.solve(arr, x))
        t -= 1