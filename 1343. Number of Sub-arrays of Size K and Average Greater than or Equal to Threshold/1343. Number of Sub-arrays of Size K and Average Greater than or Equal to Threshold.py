class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    
        count = 0
        s = 0
        for i in range(0, k-1):
            s += arr[i]

        cut_off = threshold * k
        for r in range(k-1, len(arr)):
            s += arr[r]
          
           
            if s >= cut_off:
                count += 1
            s -= arr[r-k+1]

        return count