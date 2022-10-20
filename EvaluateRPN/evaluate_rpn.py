class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        another_stack = []
        for x in tokens:
            if x == '*':
                num1 = another_stack.pop()
                num2 = another_stack.pop()
                result = num2 * num1
                another_stack.append(result)
            elif x == '/':
                num1 = another_stack.pop()
                num2 = another_stack.pop()
                result = int(num2 / num1)
                another_stack.append(result)
            elif x == '+':
                num1 = another_stack.pop()
                num2 = another_stack.pop()
                result = num2 + num1
                another_stack.append(result)
            elif x == '-':
                num1 = another_stack.pop()
                num2 = another_stack.pop()
                result = num2 - num1
                another_stack.append(result)
            else:
                another_stack.append(int(x))

        return another_stack[0]