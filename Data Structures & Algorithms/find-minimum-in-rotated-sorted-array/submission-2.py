class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = 1001

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                min_val = min(nums[r], min_val)
                l = m + 1
            elif nums[m] < nums[l]:
                min_val = min(nums[m], min_val)
                r = m - 1
            else:
                min_val = min(nums[l], min_val)
                break

        return min_val if len(nums) > 1 else nums[0]