class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #sum of two side should always be greater than third side
        nums.sort()
        nums.reverse()
        for i in range(len(nums)-2):
            base,side1,side2 = nums[i],nums[i+1],nums[i+2] 
            if side1+side2>base:
                return side1+side2+base
        return 0
        