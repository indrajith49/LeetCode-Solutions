---------------------------CORE IDEA----------------------

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_p = len(p)
        len_s = len(s)

        count_p = [0] * 26
        window_count = [0] * 26

        if len_s < len_p:
            return res
        for ch in p:
            count_p[ord(ch) - ord("a")] += 1


        for i in range(len_p):
            window_count[ord(s[i]) - ord("a")] += 1

        return window_count


sol = Solution()
print(sol.findAnagrams("cbaebabacd", p = "abc"))
