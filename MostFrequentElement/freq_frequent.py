class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 0
        result = 0
        total = 0
        n = len(nums)
        
        while right < n:
            
            total += nums[right]
            
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
                
            result = max(result, right - left + 1)
            
            right += 1
            
        return result
                    
                