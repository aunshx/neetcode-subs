class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const helper = (c) => {
            const code = c.charCodeAt(0);
            if (!(code > 47 && code < 58) &&
                // upper alpha (A-Z)
                !(code > 64 && code < 91) &&
                // lower alpha (a-z)
                !(code > 96 && code < 123)) {
            return false;
            }
            return true
        } 

        if (s.length < 2) return true
        let l = 0, r = s.length-1
        while(l<r){
            if (!helper(s[l])) l += 1
            else if (!helper(s[r])) r -= 1
            else if (s[l].toLowerCase() == s[r].toLowerCase()) {
                l += 1
                r -= 1
            } else return false
        }
        return true
    }
}
