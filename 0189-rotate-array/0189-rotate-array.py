class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums


        for i in range(k):
            n = nums.pop()
            nums.insert(0,n)

        return nums


        
        