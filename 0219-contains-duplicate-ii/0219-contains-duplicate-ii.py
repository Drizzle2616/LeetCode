class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hp = {}
        for idx,element in enumerate(nums):
            if element in hp.keys() and abs(hp[element]-idx)<=k:
                return True
            hp[element] = idx
        return False

        