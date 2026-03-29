class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0 for _ in range(len(nums))]
        prev = 1
        for i,n in enumerate(nums):
            pre[i] = prev
            prev *= n
        
        suf = [0 for _ in range(len(nums))]
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = prev
            prev *= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res
