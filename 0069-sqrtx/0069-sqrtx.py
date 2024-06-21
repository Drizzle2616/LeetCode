class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        else:
            i = 1 
            sq = 1 
            while x >= sq:
                i = i + 1
                sq = i * i
        return int(i - 1)
