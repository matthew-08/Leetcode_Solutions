## Naive solution:
## Run a linear search on the matrix and perform binary search on each subarray.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
            for i in range(len(matrix)):
                array = matrix[i]
                left = 0
                right = len(array) - 1

                while left <= right:
                    mid = (left + right) // 2
                    if array[mid] > target:
                        right = mid - 1
                    elif array[mid] < target:
                        left = mid + 1
                    else: return True
            return False
## My first (extremely lengthy and ridiculous) optimized solution.
## Here, I'm first going to the subarray at the middle position of the the matrix.
## I then determine:
## Is the lowest value of this subarray greater or equal to the target
## and
## Is the highest value of this subarray less than or equal to the target
## If it is, then we know that our value is somewhere in this subarray and we can run a binary search on it
## If it is not, we'll look at the left of the subarray and right of the subarray and compare those
## position's respective values to the target to determine whether or not we should move to
## a subarray one tier lower or a subarray one tier higher.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
            mLeft = 0
            mRight = len(matrix) - 1
            arrayToSearch = 0
            while mLeft <= mRight:
                mMid = (mLeft + mRight) // 2
                array = matrix[mMid]
                left = 0
                right = len(array) - 1

                if array[left] <= target and array[right] >= target:
                    arrayToSearch = matrix[mMid]
                    break
                else:
                    arrayToSearch = matrix[mMid]
                    if target < array[left]:
                        mRight = mMid - 1
                    else:
                        mLeft = mMid + 1
            left = 0
            right = len(arrayToSearch) - 1

            while left <= right:
                mid = (left + right) // 2
                if arrayToSearch[mid] < target:
                    left = mid + 1
                elif arrayToSearch[mid] > target:
                    right = mid - 1
                else: return True
            return False