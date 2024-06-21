class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list_ = []
        a = 0
        for i in range(len(digits)):
            c = len(digits) - i -1
            a = a + pow(10,i)*digits[c]
        s = a + 1
        for i in range(len(str(s))):
            list_.append(int(str(s)[i]))
        return list_


