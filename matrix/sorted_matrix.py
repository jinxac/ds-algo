#code

class Solution:
    def solve(self, arr):
        def merge(start, end):
            mid = (start + end) // 2
            i = start
            j = mid + 1
            temp = []

            while i <= mid and j <= end:
                if arr[i] < arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= end:
                temp.append(arr[j])
                j += 1

            print("here...", temp)

            for i in range(len(temp)):
                arr[start + i] = temp[i]


        def traverse(start, end):
            if start < end:
                mid = (start + end) // 2
                traverse(0, mid)
                traverse(mid + 1, end)
                merge(start, end)


        return traverse(0, len(arr) - 1)


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        arr = input().split()
        s = Solution()
        print(s.solve(arr))
        t -= 1
