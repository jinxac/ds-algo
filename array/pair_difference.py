#code
class Solution:
    def solve(self, arr, n):
        temp = {arr[i]: i for i in range(len(arr))}
        for i in range(len(arr)):
            diff = n - arr[i]
            if abs(diff) in temp and temp[abs(diff)] != i:
                return 1

        return -1


if __name__ == "__main__":
    t = int(input())

    while t:
        l, n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        s = Solution()
        print(s.solve(arr, 1))
        t -= 1
