func twoSum(nums []int, target int) []int {
    // val, index
    m := make(map[int]int)   
    for i := 0; i < len(nums); i++ {
        v, prs := m[target-nums[i]]
        if prs {
            return []int{v, i}
        }
        m[nums[i]] = i
    }
    return []int{0,0}
}
