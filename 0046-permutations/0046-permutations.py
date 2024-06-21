class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            # If the current permutation is complete
            if start == len(nums):
                result.append(nums[:])  # Append a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the starting element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse on the next part of the list
                backtrack(start + 1)
                # Swap back to backtrack
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack()
        return result