class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        list1=list(s)
        for i in range(len(s)):
            if(len(stack)==0):stack.append([s[i],i])
            elif(stack[-1][0]=="(" and s[i]==")"):
                list1[stack[-1][1]]=True
                list1[i]=True
                stack.pop()
            else:stack.append([s[i],i])
        ctr,max1=0,0
        for i in list1:
            if i==True:
                ctr+=1
                max1=max(max1,ctr)
            else:ctr=0
        return max1

            