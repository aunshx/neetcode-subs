class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {string}
     */
    mergeAlternately(word1, word2) {
        let i = 0
        let s = ''
        while(i < (word1.length && word2.length)){
            s += word1.charAt(i)
            s += word2.charAt(i)
            i++
        }
        s += word1.slice(i,word1.length)
        s += word2.slice(i,word2.length)
        return s
    }
}
