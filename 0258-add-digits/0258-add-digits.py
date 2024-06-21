class Solution:
    def digitSum(self,n: int)->int:
        tot=0
        while(n>0):
            tot+=n%10
            n//=10
        return tot

    def addDigits(self, num: int) -> int:
        while(num//10>0):
            num=Solution.digitSum(self,num)
        return num