class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        prefix_num = 1
        postfix_num = 1
        answer = []
        for num in nums:
            prefix_num *= num
            prefix.append(prefix_num)
        for i in range(len(nums) - 1, -1, -1):
            postfix_num *= nums[i]
            postfix.append(postfix_num)
        right = 0
        left = 0
        for i in range(len(nums)):
            if i == 0:
                left = 1
            else: 
                left = prefix[i-1]
                
            if i == (len(nums)-1):
                right = 1
            else:
                right = postfix[len(nums) - 2 -i]
                
            answer.append(left * right)

        return answer