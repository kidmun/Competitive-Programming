class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        answer = []
        
        for num in nums:
            count = 0
            for other_num in nums:
                if other_num < num:
                    count += 1
            answer.append(count)
        return answer
                