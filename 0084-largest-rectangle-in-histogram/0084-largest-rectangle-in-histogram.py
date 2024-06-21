class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i , h in enumerate(heights):
            idx = i
            if not stack:
                stack.append([i , h])
                continue
            while stack and stack[-1][1] > h:
                idx , he = stack.pop()
                max_area = max(max_area , (i - idx ) * he)
            stack.append([idx , h])

        while stack:
            idx , he = stack.pop()
            max_area = max(max_area , (i - idx + 1) * he) 
        return max_area