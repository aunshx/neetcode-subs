class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mEnd = m-1
        nEnd = n-1
        nums1End = m+n-1

        while nEnd >= 0 and mEnd >= 0:
            if nums1[mEnd] > nums2[nEnd]:
                nums1[nums1End] = nums1[mEnd]
                mEnd -= 1
            else:
                nums1[nums1End] = nums2[nEnd]
                nEnd -= 1
            nums1End -= 1

        while nEnd >= 0:
            nums1[nums1End] = nums2[nEnd]
            nEnd -= 1
            nums1End -= 1

        