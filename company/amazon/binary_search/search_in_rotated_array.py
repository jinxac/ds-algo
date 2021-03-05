class Solution:
    def get_pivot(self, A):
        start = 0
        end = len(A) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if mid > start and A[mid - 1] > A[mid]:
                return mid - 1
            
            if mid < end and A[mid + 1] < A[mid]:
                return mid + 1
            
            if A[mid] > A[start]:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
    
    def binary_search(self, A, start, end, target):
        left = start
        right = end
        
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
            
            if A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
            
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = self.get_pivot(A)
        
        if pivot == -1:
            return self.binary_search(A, 0, len(A) - 1, B)
        
        if A[pivot] == B:
            return pivot
        

        if B > A[0]:
            return self.binary_search(A, 0, pivot - 1, B)
        
        return self.binary_search(A, pivot + 1, len(A) - 1, B)
            
        
        

