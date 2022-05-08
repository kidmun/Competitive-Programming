class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        mid = len(changed) // 2 
        n = len(changed)
        if n % 2:
            return []
        
        count = Counter(changed)
        changed.sort()
        original = []
        
        for num in changed:
            
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                original.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1
                original.append(num)
                   
            
        if len(original) == mid:
            return original
        else:
            return []
        
            
        