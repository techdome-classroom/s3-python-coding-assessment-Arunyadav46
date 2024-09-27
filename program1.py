
        
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







    



  

