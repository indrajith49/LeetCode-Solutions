class Solution:
    def isAnagram(self,s, t):
        if len(s)!=len(t):
            return False

        seen = {}

        for char in t:
            seen[char] = seen.get(char, 0)+1


        for char in s:
            if char not in seen:
                return False
            seen[char] -=1
            if seen[char]<0:
                return False
            
        return True
