class Solution:
    def numDecodings(self, s: str) -> int:
        def rec(ind):
            if ind>=len(s):
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            l,r=0,0
            if s[ind]!='0':
                l=rec(ind+1)
                if ind+1<len(s) and 10<= int(s[ind]+s[ind+1]) <=26:
                    r=rec(ind+2) 
            dp[ind]=l+r
            return dp[ind]

        dp=[-1]*len(s)
        return rec(0)                  