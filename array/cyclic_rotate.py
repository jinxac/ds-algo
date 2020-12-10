#code
class Solution:
    def solve(self, arr, n, k):
        res = ""
        for i in range(n):
            res +=  str(arr[(k + i) % n]) + " "

        return res

        # 1 , 2 , 3 , 4, 5


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        s = Solution()
        k = n - 1
        print(s.solve(arr, n, k))

        t -= 1