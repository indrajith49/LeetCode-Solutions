class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        count = [0]*26
        res = 0
        for right in range(len(s)):
            char_index = ord(s[right]) - ord('A')
            count[char_index]+=1
            max_freq = max(max_freq, count[char_index])

            while (right - left + 1)-max_freq>k:
                left_char_index = ord(s[left]) - ord('A')
                count[left_char_index]-=1
                left+=1

            res = max(res, right-left+1)

        return res