class Solution:

    def find_pivot(self, nums):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if mid < end and nums[mid+1] < nums[mid]:
                return mid + 1

            if mid > start and nums[mid-1] > nums[mid]:
                return mid - 1

            if nums[start] < nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def binary_search(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def rotated_search(self, nums, pivot, target):
        start = 0
        end = len(nums) - 1

        if pivot == -1:
            return self.binary_search(nums, start, end, target)

        if target == nums[pivot]:
            return pivot

        if target < nums[0]:
            start = pivot + 1

        elif target >= nums[0]:
            end = pivot - 1


        return self.binary_search(nums, start, end, target)



    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        return self.rotated_search(nums, pivot, target)
