class Solution:
    def __init__(self):
        self._max_time = -1
        
    def calculate_max_time(self, A):
        hour = A[0] * 10 + A[1]
        minutes = A[2] * 10 + A[3]
        if hour < 24 and minutes < 60:
            self._max_time = max(self._max_time, hour  * 60 + minutes)
        
    
    def generate_permutations(self, A):
        def permute(first):
            if first == len(A):
                self.calculate_max_time(A)
            
            for i in range(first, len(A)):
                A[first], A[i] = A[i], A[first]
                permute(first + 1)
                A[first], A[i] = A[i], A[first]
        
        permute(0)
            
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perms = self.generate_permutations(A)            
        
        if self._max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(self._max_time // 60, self._max_time % 60)
