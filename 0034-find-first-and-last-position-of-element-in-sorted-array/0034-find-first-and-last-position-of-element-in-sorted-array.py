class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        bisect_left = bisect.bisect_left
        # def bisect_left(A,t):
        #     l,r = 0, len(A)
        #     while l<r:
        #         m = l + (r-l)//2
        #         if t <= A[m]:
        #             r = m
        #         else:
        #             l = m + 1
        #     return l

        if len(nums) == 0:
            return [-1,-1]

        a = bisect_left(nums, target)        
        if a<0 or a>=len(nums) or nums[a] != target:
            return [-1,-1]

        b = bisect_left(nums, target+1)
        b = b-1
        if b<0 or b>=len(nums) or nums[b] != target:
            return [-1,-1]

        return [a,b] 