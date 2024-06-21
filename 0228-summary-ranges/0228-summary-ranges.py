class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else: 
            first = nums[0]
            second = 0
            output = []
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] != 1:
                    second = nums[i-1]
                    if first==second:
                        string = str(first)
                    else:
                        string = str(first) + "->" + str(second)
                    output.append(string)
                    first = nums[i]
                if first == nums[-1]:
                    string = str(first)
                    output.append(string)
                if nums[i] == nums[-1] and nums[i]!=first:
                    string = str(first) + "->" + str(nums[i])
                    output.append(string)
            return output

            