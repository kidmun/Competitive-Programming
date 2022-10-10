class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        new_list = []
        for num in nums:
            if num != 0:
                new_list.append(num)
            else:
                count += 1
        for i in range(count):
            new_list.append(0)
        for i in range(len(new_list)):
            nums[i] = new_list[i]