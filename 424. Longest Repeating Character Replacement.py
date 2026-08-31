class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # store highest frequency of any single char inside current sliding window
        max_freq = 0
        # left pointer of sliding window, marks start of window
        left = 0
        # frequency array for uppercase A‑Z, index 0 = A, 25 = Z
        count = [0]*26
        # store answer: length of longest valid substring we found
        res = 0

        # right pointer expands window, iterate every character in string s
        for right in range(len(s)):
            # convert current character s[right] to 0‑25 array index
            char_index = ord(s[right]) - ord('A')
            # increase frequency count for this character (add char into window)
            count[char_index] += 1
            # update max_freq if current character's count is bigger
            max_freq = max(max_freq, count[char_index])

            # window_size − max_freq = number of characters we need to flip
            # if flip cost > k: we exceed allowed replacements → window invalid, shrink it
            while (right - left + 1) - max_freq > k:
                # get index of character at left edge of window
                left_char_index = ord(s[left]) - ord('A')
                # remove this left‑side character out of window: decrease its frequency
                count[left_char_index] -= 1
                # move left pointer rightwards → shrink window size by one
                left += 1

            # after window becomes valid, update our answer with current window length
            res = max(res, right-left+1)
        
        # return maximum length found
        return res
