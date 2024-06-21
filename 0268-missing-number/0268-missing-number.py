class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left,right=0,len(nums)
        nums.sort()
        while left<=right:
            mid=(left+right)//2
            if mid>len(nums)-1:
                return mid
            elif mid!=nums[mid] and mid<len(nums):
                right=mid-1
            elif mid==nums[mid]:
                left=mid+1
        return left                
        