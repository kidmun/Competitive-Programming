class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        chalk_number = k % total

        while True:
            for i in range(len(chalk)):
                chalk_number -= chalk[i]
                if chalk_number < 0:
                    return i