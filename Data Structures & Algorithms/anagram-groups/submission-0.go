func groupAnagrams(strs []string) [][]string {
    m := make(map[[26]int][]string)

    for _, s := range strs {
        var count [26]int
        for _, c := range s {
            count[c-'a']++
        }
        m[count] = append(m[count], s)

    }

    var result [][]string
    for _, g := range m {
        result = append(result, g)
    }
    return result
}
