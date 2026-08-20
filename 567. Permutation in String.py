class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        sorted_s1 = sorted(s1)

        for ch in range(len(s2)):
            if sorted_s1==sorted(s2[ch:ch+len(s1)]):
                return True
        return False
sol = Solution()
print(sol.checkInclusion("ab","eidpaooo"))