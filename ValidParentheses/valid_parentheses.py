class Solution:
    def isValid(self, s: str) -> bool:
        
        def reverse(bracket):
            
            if bracket == "(":
                return ")"
            elif bracket == "[":
                return "]"
            else:
                return "}"
        
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                
                reversed_brack = reverse(bracket)
                stack.append(reversed_brack)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if bracket != stack.pop():
                        return False
        return len(stack) == 0
                        
                
                
            