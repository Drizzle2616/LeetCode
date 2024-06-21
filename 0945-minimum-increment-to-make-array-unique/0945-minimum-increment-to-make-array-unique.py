from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment
        return moves

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 2, 2]
print(solution.minIncrementForUnique(nums1))  # Output: 1

# Example 2
nums2 = [3, 2, 1, 2, 1, 7]
print(solution.minIncrementForUnique(nums2))  # Output: 6
