class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        power = 0
        num = 0
        while num <= n:
            num = 2 ** power
            power += 1
            if num == n:
                return True
        return False
        