class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */

    validPalindrome(s) {
        let l = 0, r = s.length - 1
        while(l<r){
            if(s[l] !== s[r]) return (
                this.isPalindrome(s, l + 1, r) ||
                this.isPalindrome(s, l, r - 1)
            )
            l++
            r--
        }
        return true
    }
    isPalindrome(s, l, r){
        while(l<r){
            if(s[l] !== s[r]) return false
            l++
            r--
        }
        return true
    }
}
