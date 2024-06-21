class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = s[::-1]
        w = i.find(' ')
        if w != -1:
            return w
        else:
            return len(s)