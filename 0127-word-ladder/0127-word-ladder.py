class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        """
        approach:
        1. make the adjacency list
        2. run bfs
        """
        wordList.insert(0, beginWord)
        wordList = set(wordList)
        visitedDic = {}
        
        if endWord not in wordList:
            return 0
        
        for i in wordList:
            visitedDic[i]=0
        
        dic = defaultdict(list)
        
        for i in (wordList):
                diff = self.helper(i,wordList)
                
                dic[i]=diff
        
        # now we need to do the BFS
        q = collections.deque()           # POP(0) is O(N) is normal list, in deque it is O(1)
        q.append(beginWord)
        ans = 0
        
        while q:
            size = len(q)
            ans += 1
            for i in range(size):
                curr = q.popleft()
                visitedDic[curr] = 1
                
                if curr == endWord:
                    return ans
                
                for j in dic[curr]:
                    if visitedDic[j]==0:
                        q.append(j)
        return 0
                
    
    
    def helper(self, s, wordList):
        diff = 0
        l = set()
        for i in range(len(s)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                temp = s[0:i]+j+s[i+1:]
                # temp[i] = j
                # word = ''.join(temp)
                if temp!=s and  temp in wordList:
                    l.add(temp)

        return l