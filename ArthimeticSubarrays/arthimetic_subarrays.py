class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        result = []
        for index in range(len(l)):
            
            left = l[index]
            right = r[index]
            
            flag = True
            new_nums = nums[left:right + 1]
            
            if len(new_nums) > 1:
                new_nums.sort()
                diff = new_nums[1] - new_nums[0]
            
                for i in range(len(new_nums)-1):
                    if new_nums[i+1] - new_nums[i] != diff:
                        flag = False
            else:
                flag = False
                    
            
                        
            if flag:
                result.append(True)
            else:
                result.append(False)
        return result
                