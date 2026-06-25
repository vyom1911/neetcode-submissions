class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        anagrams = defaultdict(list)
        for st in strs:
            sorted_str = "".join(sorted(st))
            anagrams[sorted_str].append(st)
        return list(anagrams.values())