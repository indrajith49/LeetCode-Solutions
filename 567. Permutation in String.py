

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        sorted_s1 = sorted(s1)

        for ch in range(len(s2)):
            if sorted_s1==sorted(s2[ch:ch+len(s1)]):
                return True
        return False
sol = Solution()
print(sol.checkInclusion("ab","eidpaooo"))

-------------------------------------MORE OPTIMIZED-------------------------
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        # frequency arrays for 'a'..'z'
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for ch in s1:
            cnt1[ord(ch) - 97] += 1
        for i in range(m):
            cnt2[ord(s2[i]) - 97] += 1

        if cnt1 == cnt2:
            return True

        # slide the window over s2
        for i in range(m, n):
            cnt2[ord(s2[i]) - 97] += 1            # add new char
            cnt2[ord(s2[i - m]) - 97] -= 1        # remove char leaving window
            if cnt1 == cnt2:
                return True

        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidpaooo"))
