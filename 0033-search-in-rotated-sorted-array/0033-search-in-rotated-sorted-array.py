class Solution:
    def search(self, nums: list[int], target: int) -> int:
        z = nums
        if target in nums : 
            return  z.index(target)
        else : 
            return -1