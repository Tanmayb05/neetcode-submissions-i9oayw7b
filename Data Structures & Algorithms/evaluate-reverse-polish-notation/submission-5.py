class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mapping = ["+", "*", "-", "/"]
        for i in tokens:
            if i in mapping:
                b = stack.pop()
                a = stack.pop()
                print(a,b)
                if i == "+":
                    stack.append(int(a)+int(b))
                elif i == "-":
                    stack.append(int(a)-int(b))
                elif i == "*":
                    stack.append(int(a)*int(b))
                elif i == "/":
                    stack.append(int(a)/int(b))
            else:
                stack.append(i)
                print(f"stack: {stack[-1]}")
        return int(stack[-1])