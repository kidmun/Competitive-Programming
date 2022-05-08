class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        new_list = []
        
        for num in nums:
            
            new_list.append(int(num))
        
        new_list.sort()
        
        answer = str(new_list[k*-1])
        
        return answer