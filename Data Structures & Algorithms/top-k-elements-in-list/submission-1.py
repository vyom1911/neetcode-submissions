class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for n in nums:
            frequency[n]+=1
        
        order_dict = dict(sorted(frequency.items(),key=lambda item: item[1],reverse=True))
        return list(order_dict.keys())[:k]