class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            total = nums[left] + nums[right]
            
            if total == k:
                left += 1
                right -= 1
                count += 1
            elif total > k:
                right -= 1
            else:
                left += 1
        return count
                        