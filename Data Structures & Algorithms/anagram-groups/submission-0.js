class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = {};
        for (let s of strs) {
            const m = new Array(26).fill(0);
            for (let c of s) {
                m[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
            }
            const key = m.join(',');
            if (!map[key]) {
                map[key] = [];
            }
            map[key].push(s);
        }
        return Object.values(map);
    }
}
