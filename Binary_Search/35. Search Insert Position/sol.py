class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        result = 0
        while left <= right:
            mid = (left + right) // 2
            result = mid
            if nums[mid] < target:
                left = mid + 1
            else: right = mid - 1
        if result == 0 and nums[result] > target:
            return 0
        if nums[result] < target:
            return result + 1
        else: return result