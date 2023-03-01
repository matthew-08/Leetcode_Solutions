class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        windowLeft = 0
        minValue = 100000000000
        wCount = 0
        for i in range(len(blocks)):
            if blocks[i] == "W":
                wCount += 1
            if i >= k - 1:
                print(wCount)
                minValue = min(minValue, wCount)
                if blocks[windowLeft] == "W":
                    wCount -=1
                windowLeft += 1
        return minValue

               #Window left and window right start at index 0
               #Expand window right until it is equal to the length of k
               #At that point, count our 