class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        start = 0
        end = len_nums1
        
        while start <= end:
            partition_nums1 = (start + end) // 2
            partition_nums2 = ((len_nums1 + len_nums2 + 1) // 2) - partition_nums1
            
            max_left_nums1 = float('-inf')
            min_right_nums1 = float('inf')
            max_left_nums2 = float('-inf')
            min_right_nums2 = float('inf')
            
            if partition_nums1 > 0:
                max_left_nums1 = nums1[partition_nums1 - 1]
            
            if partition_nums1 < len_nums1:
                min_right_nums1 = nums1[partition_nums1]
                
            if partition_nums2 > 0:
                max_left_nums2 = nums2[partition_nums2 - 1]
            
            if partition_nums2 < len_nums2:
                min_right_nums2 = nums2[partition_nums2]
            
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if ((len_nums1 + len_nums2) % 2) == 0:
                    return float(max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                end = partition_nums1 - 1
            else:
                start = partition_nums1 + 1

