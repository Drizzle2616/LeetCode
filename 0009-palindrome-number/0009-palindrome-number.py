class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        inv = a[::-1]
        if inv == a:
            return True
        else:
            return False
            
