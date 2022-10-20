class Solution:
    def reverseParentheses(self, s: str) -> str:
        first_stack = []
        
        for char in s:
            if char == "(":
                first_stack.append(char)
            elif char == ")":
                flag = True
                second_stack = []
                while flag:
                    num = first_stack.pop()
                    if num != '(':
                        second_stack.append(num)
                    else:
                        
                        for x in second_stack:
                            first_stack.append(x)
                        flag = False
            else:
                first_stack.append(char)
        
        answer = ""
        for i in first_stack:
            answer += i
        return answer  
