class Solution:
    def findTwoElement( self,arr, n):
        start = 0
        result = []

        while start < len(arr):
            correct_pos = arr[start] - 1

            if arr[start] != arr[correct_pos]:
                arr[correct_pos], arr[start] = arr[start], arr[correct_pos]
            else:
                start += 1

        for i in range(len(arr)):
            if arr[i] != i + 1:
                result.append(arr[i])
                result.append(i + 1)

        return result
