class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        #We are assured that,  We will have atleast 1 element.
        maxSum = curSum = nums[0]

        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(maxSum, curSum)

        return maxSum