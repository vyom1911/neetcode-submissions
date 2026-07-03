class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []

        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                try:
                    int_val = int(t)
                except ValueError:
                    raise
                op_stack.append(int(t))
    
            else:
                b = op_stack.pop()
                a = op_stack.pop()

                if t == "+":
                    op_stack.append(a + b)
                elif t == "-":
                    op_stack.append(a - b)
                elif t == "*":
                    op_stack.append(a * b)
                elif t == "/":
                    op_stack.append(int(a / b))
                else:
                    raise ValueError("Unexpected Operand")
        return op_stack[-1]
