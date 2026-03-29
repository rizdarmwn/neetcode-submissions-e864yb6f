class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, n in enumerate(nums):
            n2 = target - n
            if dct.get(n2, None) is not None and dct[n2] != i:
                return [dct[n2], i]
            dct[n] = i
        return [0,0]
        

