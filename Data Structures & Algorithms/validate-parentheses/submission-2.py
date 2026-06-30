class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        close_to_open = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in close_to_open:
                if stack and stack.pop()==close_to_open[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True