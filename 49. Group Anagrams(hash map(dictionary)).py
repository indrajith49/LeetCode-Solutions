from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Edge case: empty input
        if not strs:
            return []

        result = {}
        # Dictionary: key = sorted string, value = list of original strings
        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s in result:
                result[sorted_s].append(s)
            else:
                result[sorted_s] = [s]

        return list(result.values())



# Test
sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


ALTERNATIVE -----------------------------------------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs):

        if not strs:
            return  []

        result = {}
        for char in strs:
            sorted_s = ''.join(sorted(char))
            result[sorted_s] = result.get(sorted_s, []) + [char]

        return list(result.values())



        

