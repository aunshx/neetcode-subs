class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1, m, nums2, n) {
        let last = nums1.length - 1
        let i = m-1
        let j = n-1
        while( j>= 0){
            if(i>=0 && nums1[i] > nums2[j]){
                nums1[last--] = nums1[i--]
            } else {
                nums1[last--] = nums2[j--]
            }
        }
    }
}
