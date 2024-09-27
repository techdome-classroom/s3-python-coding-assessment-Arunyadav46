import unittest
from program1 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_mixed_parentheses(self):
        self.assertFalse(self.solution.isValid("(){"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

def isValid(s: str) -> bool:
    stack = []
    

    bracket_map = {')': '(', '}': '{', ']': '['}
    
   
    for char in s:
 
        if char in bracket_map:
            
            top_element = stack.pop() if stack else '#'
            
            # If the popped element doesn't match the corresponding opening bracket, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # After traversing the string, the stack should be empty if the string is valid
    return not stack

