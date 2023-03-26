class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                result.insert(0, nums[left]**2)
                left +=1
            else:
                result.insert(0, nums[right]**2)
                right -= 1
        return result
