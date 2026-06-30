class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        sorted_nums = sorted(nums)

        count_consecutive = 1
        max_count = 0
        for i in range(1,len(nums)):
            
            if sorted_nums[i]-sorted_nums[i-1]>1:
                if count_consecutive>max_count:
                    max_count = count_consecutive
                count_consecutive=1
            elif sorted_nums[i]-sorted_nums[i-1]==0:
                continue
            else:
                count_consecutive+=1
        if count_consecutive>max_count:
            max_count = count_consecutive
        return max_count