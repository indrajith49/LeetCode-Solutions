----------------------------------------------CORE IDEA-------------------------------------

we can use counter and also can sort to check whether the two strings are equal or not. game over
But counter is more effecient  than other methods





-------I WILL REVIEW THIS CODE NEXT TIME ALTHOUGH THIS SEEMS TO BE EASY. THIS IS JUST HASHING AND THEN COMPARING BY ELIMINATING ALL NUMBERS FROM THE SECOND STRING. IF THE STRING IS EMPTY RETURN TRUE. HOWEVER I WILL REVIEW THIS CODE LATER
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
