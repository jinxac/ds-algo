class Solution:
    def countSquares(self, N):
        # code here
        start = 1
        end = N

        while start <= end:
            mid = (start + end) // 2

            if mid * mid == N:
                return mid - 1

            if mid * mid < N:
                start = mid + 1
            else:
                end = mid - 1

        return start - 1