----------------------------------CORE IDEA--------------------------------------
For each position, 
the answer = (product of all numbers on the LEFT) × (product of all numbers on the RIGHT)

1. Prefix (Left Products): Start with 1. Walk from left to right. 
   At each position, store the product of all numbers to the left in the result array. 
   Then update the prefix to include the current number for the next position.

2. Suffix (Right Products): Start with 1. Walk from right to left.
   At each position, multiply the already-stored left product by the product of all numbers to the right.
   Then update the suffix to include the current number for the next position.

3. Game Over: The result array now contains the final answer — the product of all numbers except the current one.


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            new[i] = prefix
            prefix*=nums[i]
        
        #After this loop:
        #new = [1,1,2,6]
        #this is the left product for each position

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            new[i] *= suffix #also multiplying with the current value of each position of new.
            suffix*=nums[i]
            
        #new = [24,12,8,6]
        #this is the left * right = final answer
        
        return new



      --->>>next time if I am able to understand this 
            and solve this problem without looking at the answer and by only knowing the core idea! 
            I will write something below this line. Today's date is 05/08/2026
  can i solve this now finally? i have been trying to undertsand this problem for almost 1 year.
  From the mid of 2025. Let me know in the answer
ANSWER = [.........]

