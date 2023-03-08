class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        if(len(nums) == 1):
            return [nums.copy()]
        
        for i in range(len(nums)):
            val = nums.pop(0)
            permutation = self.permute(nums)

            for perm in permutation:
                perm.append(val)
            result.extend(permutation)
            nums.append(val)
        
        return result