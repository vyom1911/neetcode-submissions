class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        anagrams = defaultdict(list)
        for st in strs:
            count = [0]*26
            for char in st:
                count[ord(char)-ord('a')]+=1
            anagrams[tuple(count)].append(st)
        return list(anagrams.values())