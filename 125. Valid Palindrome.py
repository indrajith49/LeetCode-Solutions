class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = []

        for char in s:
            if char.isalnum():
                answer.append(char.lower())
                

        if answer == answer[::-1]:
            return True
        else:
            return False
