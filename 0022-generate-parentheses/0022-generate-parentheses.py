class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        aws = {"()"}
        for _ in range(n-1):
            tmp = set()
            for j in aws:
                for k in range(len(j)+1):
                    tmp.add(j[:k]+"()"+j[k:])
            aws = tmp
        return [i for i in aws]