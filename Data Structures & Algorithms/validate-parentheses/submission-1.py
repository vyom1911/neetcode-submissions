class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for st in s:
            if st in ["(","{","["]:
                stack.append(st)
            elif stack and st == ")" and stack.pop() == "(":
                continue
            elif stack and st == "}" and stack.pop() == "{":
                continue
            elif stack and st == "]" and stack.pop() == "[":
                continue
            else:
                return False
        if stack:
            return False
        else:
            return True