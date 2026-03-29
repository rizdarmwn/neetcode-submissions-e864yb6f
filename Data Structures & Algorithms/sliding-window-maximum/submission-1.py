class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        res = []
        l, r = 0, 0

        first_max = float('-inf')
        while r < k:
            first_max = max(first_max, nums[r])
            r += 1
        res.append(first_max)
        l += 1
        while r < len(nums):
            temp_max = float('-inf')
            l2, r2 = l, r
            while r2 >= l2:
                temp_max = max(temp_max,max(nums[r2], nums[l2]))
                l2 += 1
                r2 -= 1
            res.append(temp_max)
            r+=1
            l+=1
        
        return res
