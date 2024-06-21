class Solution:
    def subsets(self, a: List[int]) -> List[List[int]]:
        return reduce(lambda b,v:b+[c+[v] for c in b],a,[[]])