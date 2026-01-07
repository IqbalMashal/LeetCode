class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        inds = {}

        for i, n in enumerate(nums):
            inds[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in inds.keys() and inds[diff] != i:
                return [i,inds[diff]]

        return []
        