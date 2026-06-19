class Solution:
    def isValid(self, s: str) -> bool:
        #first add characters to stack 
        #if the charcs are in dict append in to stack 
        #if not on dict we check if the stack is empty and pop it 
        #if the popped char is not equal to my current char, false 
        #else we return true 
        d = {"(":")", "{":"}", "[":"]"}
        stack = []

        for char in s:
            if char in d:
                stack.append(char)
            else:
                if stack == [] or d[stack.pop()] != char:
                    return False
        return True if stack ==[] else False