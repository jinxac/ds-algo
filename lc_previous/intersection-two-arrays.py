class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        
        i = 0
        j = 0
        res = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                temp = nums2[j]
                res.append(temp)
                while i < len(nums1) and nums1[i] == temp:
                    i += 1
                while j < len(nums2) and nums2[j] == temp:
                    j += 1
            elif nums2[j] > nums1[i]:
                while  i < len(nums1) and nums2[j] > nums1[i]:
                    i += 1
            else:
                while j < len(nums2) and nums1[i] > nums2[j]:
                    j += 1
        
        return res
                
