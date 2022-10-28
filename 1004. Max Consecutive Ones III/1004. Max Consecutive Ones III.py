class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,mx = 0, 0

        for right, num in enumerate(nums):
            k -= (1-num)
            if k < 0:
                k += (1-nums[left])
                left += 1
            answer = max(mx, right - left + 1)
        return answer