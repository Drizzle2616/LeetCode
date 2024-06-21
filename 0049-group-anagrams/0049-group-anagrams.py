class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [list(group) for _, group in groupby(sorted(strs, key=lambda x: sorted(x)), key=lambda x: sorted(x))]