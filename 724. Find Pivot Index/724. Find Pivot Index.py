class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
  
        for i in range(len(nums)):
            rigth_sum = total - nums[i] - left_sum      
            if left_sum == rigth_sum:
                return i 
            left_sum += nums[i]
        return -1