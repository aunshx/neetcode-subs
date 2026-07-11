class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l = 0, r = heights.length - 1, max = 0
        while(l<r){
            if(heights[l] < heights[r]){
                max = Math.max(max, heights[l]*(r-l))
                l++
            } else {
                max = Math.max(max, heights[r]*(r-l))
                r--
            }
        }
        return max
    }
}
