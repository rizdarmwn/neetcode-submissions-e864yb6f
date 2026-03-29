class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e= 0, len(nums) - 1

        while s < e:
            m = s + (e - s) // 2
            if nums[m] > nums[e]:
                s = m + 1
            else:
                e = m
            
        pvt = s

        def binary_search(l, r):
            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        res = binary_search(pvt, len(nums) - 1)

        return res if res != -1 else binary_search(0, pvt - 1)