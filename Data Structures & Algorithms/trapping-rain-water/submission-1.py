class Solution:
    def trap(self, height: List[int]) -> int:
        if (len(height) <= 2):
            return 0
        res = 0

        for i in range(1, len(height) - 1):
            l, r = i - 1, i + 1
            max_l, max_r = l, r
            while l > 0:
                l -= 1
                if (height[max_l] < height[l]):
                    max_l = l
            
            while r < len(height) - 1:
                r += 1
                if (height[max_r] < height[r]):
                    max_r = r
            # print(height[max_l], height[i], height[max_r])
            temp_res = min(height[max_l], height[max_r]) - height[i]
            # print(temp_res)
            if temp_res > 0:
                res += temp_res
        
        return res