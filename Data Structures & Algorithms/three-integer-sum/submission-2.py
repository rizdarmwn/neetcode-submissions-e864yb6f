class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                result = nums[j] + nums[k]
                target = -nums[i]
                if result > target:
                    k -= 1
                elif result < target:
                    j += 1
                elif target == result:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    
                
        return list(list(i) for i in res)