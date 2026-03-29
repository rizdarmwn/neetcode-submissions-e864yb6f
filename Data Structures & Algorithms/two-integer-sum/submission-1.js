class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map();
        for (let i = 0; i < nums.length; i++) {
            map[nums[i]] = i
        }

        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i]
            let j = map[diff]
            if (j) {
                if (i == j) continue;
                if (i < j) {
                    return [i, j]
                } else {
                    return [j, i]
                }
            }
        }

        return [0,0]
    }
}
