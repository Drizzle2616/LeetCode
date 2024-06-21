class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        stack = []

        def backtrack(i, total=0):
            if total == target:
                output.append(stack.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            stack.append(candidates[i])
            backtrack(i+1, total+candidates[i])

            stack.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, total)
        
        backtrack(0)
        return output