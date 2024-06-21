class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = 0
        seen = set()
        duplicate = -1
        
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            actual_sum += num
        
        missing = expected_sum - (actual_sum - duplicate)
        return [duplicate, missing]