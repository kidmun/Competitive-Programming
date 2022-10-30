class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        start = 0
        end = 0
        d = {}

        while end < len(fruits):
            d[fruits[end]] = end
            if len(d) >= 3:
                min_val = min(d.values())
                del d[fruits[min_val]]
                start = min_val + 1
            res = max(res, end - start + 1)
            end += 1
        return res
     