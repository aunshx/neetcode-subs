class Solution {
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    reverseString(s) {
        if (s.length < 2) return s
        let l = 0, r = s.length-1
        while(l<r){
            [s[l], s[r]] = [s[r], s[l]]
            l += 1
            r -= 1
        }
        return s
    }
}
