## brute force

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {n: i for i,n in enumerate(nums1)}
        
        result = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in hashMap:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    result[hashMap[nums2[i]]] = nums2[j]
                    break
        return result


## stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = { n: i for i,n in enumerate(nums1) }
        
        result = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            currentVal = nums2[i]
            while stack and currentVal > stack[-1]:
                num = stack.pop()
                result[hashMap[num]] = currentVal
            if currentVal in hashMap:
                stack.append(currentVal)
        return result    