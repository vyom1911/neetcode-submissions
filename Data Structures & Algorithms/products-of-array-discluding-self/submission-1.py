class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prod=1
        # zero_count=0
        # zero_index=None
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         zero_count+=1
        #         zero_index=i
        #     prod = nums[i]*prod

        # if zero_count>1:
        #     return [0]*len(nums)
        # elif zero_count==1:
        #     prod_zero = 1
            
        #     for n in nums:
        #         if n !=0:
        #             prod_zero = n * prod_zero

        #     output = [0]*len(nums)
        #     output[zero_index] = prod_zero
        #     return output

        # else:
        #     return [prod//n for n in nums]

        pref=[0]*len(nums)
        suffix=[0]*len(nums)
        res=[0]*len(nums)

        pref[0] = suffix[len(nums) - 1] = 1
        for i in range(1,len(nums)):
            pref[i] = nums[i-1]*pref[i-1]

        for i in range(len(nums)-2, -1,-1):
            suffix[i] = nums[i+1]*suffix[i+1]

        for i in range(len(nums)):
            res[i] = pref[i] * suffix[i]
        return res