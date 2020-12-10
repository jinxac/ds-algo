class Solution:
    def binary_search(self, matrix, target):
        temp = []
        for row in matrix:
            temp += row

        start = 0
        end = len(temp) - 1

        while start <= end:
            mid = (start + end) // 2
            if target == temp[mid]:
                return True

            if target < temp[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return False




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binary_search(matrix, target)
