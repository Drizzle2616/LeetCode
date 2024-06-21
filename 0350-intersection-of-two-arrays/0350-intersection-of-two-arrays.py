class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # taking two hashmaps to store the each value and its count
        hashMap1 = defaultdict(int)
        hashMap2 = defaultdict(int)
        # a list to store the value
        answerList = []

        for i in nums1:
            hashMap1[i] = hashMap1[i] + 1

        for i in nums2:
            hashMap2[i] = hashMap2[i] + 1

        # for each value in hashMap1 , if that is present in hashMap2, we append it to the answerList
        for key in hashMap1:
            if key in hashMap2:
                answerList.append(key)

        return answerList