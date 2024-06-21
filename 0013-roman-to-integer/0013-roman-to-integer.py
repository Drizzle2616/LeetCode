class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        a = 0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i + 1]]:
                a = a - d[s[i]]
            else:
                a = a + d[s[i]]
        return a + d[s[-1]]
