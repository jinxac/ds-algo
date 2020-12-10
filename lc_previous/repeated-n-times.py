class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # Approach 1 : Math logic
#         actual_sum = 0
#         total_sum = 0
#         for element in A:
#             actual_sum += element
        
#         a_set = set(A)
        
#         for element in a_set:
#             total_sum += element
        
#         if len(A) == len(a_set):
#              return None
        
#         return (actual_sum - total_sum) // (len(A) - len(a_set))
       
#     Approach 2 : Sort n compare adjancent
#         A.sort()
#         for i in range(0, len(A) - 1):
#             if A[i] == A[i+1]:
#                 return A[i]
        
#         return None
         
    # Appoach 3: Hashmap/set
         bucket = set()
         for element in A:
                if element in bucket:
                    return element
                bucket.add(element)
        
         return None
