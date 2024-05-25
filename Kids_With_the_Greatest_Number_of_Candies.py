from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        #find the max number of candies in the given list
        originalMaxCandies = max(candies)

        #build a list with as many entries as given list
        return [candy + extraCandies >= originalMaxCandies for candy in candies ]