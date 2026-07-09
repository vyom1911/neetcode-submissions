class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch,0) + 1
        
        window = {}
        
        # how many characters satisfy the required frequency
        char_correct = 0
        # Total number of unique characters we must satisfy
        unique_char = len(need)
        
        # tracking best window found : [start, end]
        best_len = float('inf')
        best_start = 0
        best_end = 0

        left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char,0) + 1

            if char in need and window[char] == need[char]:
                char_correct += 1
            
            while char_correct == unique_char:
                if right - left + 1 < best_len:
                    best_len = right-left+1
                    best_start = left
                    best_end = right
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    char_correct -= 1

                left += 1
            
        if best_len == float('inf'):
            return ""
        return s[best_start:best_end+1]