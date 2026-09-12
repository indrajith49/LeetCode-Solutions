from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l<r:
            m  = (l+r)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/m)

            if total_hours <= h:
                r = m
            else:
                l = m+1


        return l


