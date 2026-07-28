--------------------------------------------------------------------CORE IDEA--------------------------------------------------------------------

from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        mins = nums[:]          # Step 1: Track the cheapest price seen for each position
        best = sum(nums)        # Step 2: Start with cost of collecting without any rotation

        for i in range(n):      # Step 3: Try each number of rotations (0 to n-1)
            current = i * x     # Step 4: Cost of rotating i times
            
            for j in range(n):  # Step 5: Update the cheapest price for each position
                mins[j] = min(mins[j], nums[(j + i) % n])
            
            best = min(best, sum(mins) + current)  # Step 6: Update the best total cost
        
        return best
      
