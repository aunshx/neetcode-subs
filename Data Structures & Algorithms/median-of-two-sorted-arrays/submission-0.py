class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        p1 = p2 = 0
        n1= len(nums1)
        n2 = len(nums2)

        while (p1 < n1 and p2 <n2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        res.extend(nums1[p1:]) if p1 < n1 else res.extend(nums2[p2:])

        n3 = len(res)

        if n3%2 != 0:
            return res[(n3//2)]
        else:
            return (res[n3//2] + res[(n3//2)-1])/2
        
