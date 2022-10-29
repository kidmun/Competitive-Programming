class Solution:
   
    def getMaxSubarraySum(self,arr,size):
        n = len(arr)
        if n < size: return 0
        max_sum = temp_sum = sum(arr[:size])
        for i in range(1,n-size+1):
            temp_sum = temp_sum + arr[i+size-1] - arr[i-1]
            if temp_sum > max_sum:max_sum = temp_sum
        return max_sum
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        summ = sum(nums[:firstLen])
        ans = summ  + self.getMaxSubarraySum(nums[firstLen:],secondLen)   
        for i in range(1,n-firstLen+1):
            summ = summ + nums[i+firstLen-1] - nums[i-1]
            a = self.getMaxSubarraySum(nums[:i],secondLen)
            b = self.getMaxSubarraySum(nums[i+firstLen:],secondLen)
            m = a if a > b else b
            ans = max(ans, summ + m)
        return ans
 