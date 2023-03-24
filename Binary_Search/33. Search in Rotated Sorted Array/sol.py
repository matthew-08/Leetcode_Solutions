class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
    def binarySearch(self, nums, target, leftBias):

            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if leftBias:
                        right = mid - 1
                        continue
                    else:
                        left = mid + 1
                        continue
                if target > nums[mid]:
                    left = mid + 1
                else: right = mid - 1
            return result