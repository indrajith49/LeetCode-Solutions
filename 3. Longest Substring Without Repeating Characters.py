---------------------------CORE IDEA-----------------------

so the core idea is at first we will check if the the s is empty or not. 
then we will make two pointer one will stay still until it is ordered to move and another will be moving inside a loop.
then we will run a loop and then check if we have seen the current window previously by the help of a dictionary. 
if we have seen this before then we will move our left pointer one step ahead else we will keep noting it down to the seen dictionary.
and then calculate the max length.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case: empty string
        if not s:
            return 0
        
        left = 0
        max_length = 0
        seen = {}  # char -> index
        
        for right in range(len(s)):
            char = s[right]
            
            # If char already seen and is inside current window
            if char in seen and seen[char] >= left: #seen[char] is mainly the index of the current character? 
                # Move left past the duplicate
                left = seen[char] + 1
            
            # note down the latest index
            seen[char] = right
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length
