class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const mapS = new Map();
        const mapT = new Map();
        if (s.length != t.length) {
            return false;
        }
        for (let i = 0; i < s.length; i++) {
            if (mapS.has(s[i])) {
                mapS.set(s[i], mapS.get(s[i]) + 1);
            } else {
                mapS.set(s[i], 1);
            }

            if (mapT.has(t[i])) {
                mapT.set(t[i], mapT.get(t[i]) + 1);
            } else {
                mapT.set(t[i], 1);
            }
        }

        let ans = true;
        mapS.forEach((v,k) => {
            console.log(mapT.has(k));
            if (!mapT.has(k)) {
                ans = false;
            }
            
            if (mapT.has(k) && !(mapT.get(k) === v)) {
                ans = false;
            }
        })

        return ans;
    }
}
