class Solution:
    def countSegments(self, s: str) -> int:
        c=[]
        if(len(s)==0):
            return(0)
        else:
            k=s.split(" ")
            for j in k:
                if len(j)!=0:
                    c.append(j)
            return(len(c))