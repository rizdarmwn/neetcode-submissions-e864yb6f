func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    m1 := make(map[byte]int)
    m2 := make(map[byte]int)

    for i := 0; i < len(s); i++ {
        if m1[s[i]] <= 0 {
            m1[s[i]] = 1
        } else {
            m1[s[i]] = m1[s[i]] + 1
        }

        if m2[t[i]] <= 0 {
            m2[t[i]] = 1
        } else {
            m2[t[i]] = m2[t[i]] + 1
        }
    }

    for k, v := range m1 {
        if v != m2[k] {
            return false
        }
    }

    return true
}
