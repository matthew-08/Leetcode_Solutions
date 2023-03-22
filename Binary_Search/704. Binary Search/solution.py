class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0 
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1