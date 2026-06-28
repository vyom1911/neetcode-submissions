class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod=1
        zero_count=0
        zero_index=None
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
                zero_index=i
            prod = nums[i]*prod

        if zero_count>1:
            return [0]*len(nums)
        elif zero_count==1:
            prod_zero = 1
            
            for n in nums:
                if n !=0:
                    prod_zero = n * prod_zero

            output = [0]*len(nums)
            output[zero_index] = prod_zero
            return output

        else:
            return [prod//n for n in nums]