
## Failed bruteforce solution.
## The idea behind this bruteforce solution was to first sort the array from highest to lowest

## From there, we take the highest value and make it the result (it's the highest, thus we can 
## be sure the rest of the values lower than it will be eaten in one pass-through).
## This value is then pushed to a "numsPassed" array which represents all the values
## we've already iterated through.

## Now, for every piles[i], we'll take all the values lower than piles[i] and assume they'll be
## eaten in one passthrough.  This value will be saved in eatenPiles.
## Then, for all of the values in "numsPassed" (all the greater than values passed)
## We'll add to this eatenPiles variable the amount needed to eat each greater than value

## Once we've done that, we'll have calculated the amount of passthroughs needed to eat
## all piles of bananas at a speed of piles[i].

## The biggest problem with this failed solution is that it only allows for a banana-eating speed
## of values which are present in piles array.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        res = 0 
        print(piles)

        passedNums = []
        for i in range(len(piles)):
            if i == 0:
                passedNums.append(piles[i])
                res = piles[i]
                continue
            else:
                currentPile = piles[i]
                eatenPiles = len(piles) - i
                for j in passedNums:
                    amountNeeded = math.ceil(j / currentPile)
                    eatenPiles += amountNeeded
                if eatenPiles <= h:
                    passedNums.append(piles[i])
                    res = currentPile
                else:
                    break
        return res
                    