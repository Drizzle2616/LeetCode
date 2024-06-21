class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used):
            # If the current permutation is complete
            if len(path) == len(nums):
                result.append(path[:])  # Append a copy of the current permutation
                return
            
            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Mark the element as used
                used[i] = True
                path.append(nums[i])
                # Recurse with the current element included
                backtrack(path, used)
                # Backtrack by unmarking the element and removing it from the path
                used[i] = False
                path.pop()
        
        nums.sort()  # Sort the numbers to handle duplicates
        result = []
        used = [False] * len(nums)
        backtrack([], used)
        return result
