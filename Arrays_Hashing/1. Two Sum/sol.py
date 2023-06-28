class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {

        }
        for i in range(len(nums)):
            num = target - nums[i]
            if num in prev:
                return [i, prev[num]]
            prev[nums[i]] = i
        