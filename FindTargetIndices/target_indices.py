class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        def sort_array(arr):
            
            for i in range(len(arr)):
                
                for j in range(i+1,len(arr)):
                    
                    if arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
            return arr
        answer = []
        arr = sort_array(nums)
        index = 0
        for num in arr:
            if num == target:
                answer.append(index)
            index += 1
        return answer
            