# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def binarySearch(self, left: int, right: int):
        if left > right:
            return -1

        mid = left + (right-left)//2
        result = guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            return self.binarySearch(left, mid-1)
        else:
            return self.binarySearch(mid+1, right)

    def guessNumber(self, n: int) -> int:
        return self.binarySearch(1,n)
        