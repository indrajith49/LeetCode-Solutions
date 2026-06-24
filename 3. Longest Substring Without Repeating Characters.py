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
            if char in seen and seen[char] >= left:
                # Move left past the duplicate
                left = seen[char] + 1
            
            # Update last seen position
            seen[char] = right
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length
