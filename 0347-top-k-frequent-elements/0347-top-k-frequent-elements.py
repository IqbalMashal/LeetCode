class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return

        indices = {}
        most_freguent = [] 
        
        for n in nums:
            indices[n] = 1 + indices.get(n, 0)

        sorted_keys = sorted(indices, key=indices.get, reverse=True)  # Precompute sorted order

        for i in range(k):
            most_freguent.append(sorted_keys[i])  # Extract and append each top key
        
        return most_freguent