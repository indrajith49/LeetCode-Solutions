class Solution:
    def isValid(self, s):

        stack = []
        parenthesis = {']':'[', '}':'{', ')': '('}

        for char in s:
            if char in parentheses.values():
                stack.append(char)

            elif char in parentheses:
                if not stack or stack[-1]!=parenthesis[char]:
                    return False

                stack.pop()

        return not stack

sol = Solution()
print(sol.isValid("({[]})"))

--------------------------------------------------------------------example:--------------------------------------------------------------------

Step-by-Step Example: s = "({[]})"
Step 1: char = '('
'(' is not a closing bracket (it's not in parenthesis keys)

'(' is in parenthesis.values() → push to stack

stack = ['(']

Step 2: char = '{'
'{' is not a closing bracket → push to stack

stack = ['(', '{']

Step 3: char = '['
'[' is not a closing bracket → push to stack

stack = ['(', '{', '[']

Step 4: char = ']'
']' is a closing bracket (it's in parenthesis keys)

Check: stack[-1] = '[' (top of stack)

parenthesis[']'] = '[' (expected opening bracket)

'[' == '[' → match ✅

stack.pop() → removes '['

stack = ['(', '{']

Step 5: char = '}'
'}' is a closing bracket

stack[-1] = '{'

parenthesis['}'] = '{'

'{' == '{' → match ✅

stack.pop() → removes '{'

stack = ['(']

Step 6: char = ')'
')' is a closing bracket

stack[-1] = '('

parenthesis[')'] = '('

'(' == '(' → match ✅

stack.pop() → removes '('

stack = []

Step 7: return not stack
stack = [] → not [] = True ✅


another example!!!!!!!!



Let’s say your input is s = "(]".

Step 1: You see char = '('
It’s an opening bracket.

You push it onto the stack.

stack = ['(']

Step 2: You see char = ']'
It’s a closing bracket.

Now you ask: "Does the top of my stack match this closing bracket?"

Step 3: Get the top of the stack
python
stack[-1]  # This is '('
Step 4: Get the expected match for ']'
python
brackets[']']  # This is '['



||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping of closing → opening
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in brackets:  # It's a closing bracket
                if not stack:  # Stack is empty → no matching opening
                    return False
                top = stack.pop()
                if top != brackets[char]:  # Mismatch
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        # If stack is empty, all brackets matched
        return len(stack) == 0

# Test
sol = Solution()
print(sol.isValid("()"))       # True
print(sol.isValid("()[]{}"))   # True
print(sol.isValid("(]"))       # False
print(sol.isValid("([)]"))     # False
print(sol.isValid("{[]}"))     # True
