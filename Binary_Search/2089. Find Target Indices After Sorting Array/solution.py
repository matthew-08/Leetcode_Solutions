class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        low = 0
        high = len(nums)-1
        solution = []

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                solution.append(mid)
                lowC = mid - 1
                highC = mid + 1
                while lowC >= 0 and nums[lowC] == target:
                    solution.append(lowC)
                    lowC -= 1
                while highC <= len(nums) - 1 and nums[highC] == target:
                    solution.append(highC)
                    highC += 1
                break
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return sorted(solution)