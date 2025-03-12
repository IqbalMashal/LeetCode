class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = {}

        for num in nums:
            if num in unique:
                return True
            unique[num] = 1

        return False
         