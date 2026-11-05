from heapq import heapify, heappop, heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        m = {}
        for ch in s:
            m[ch] = m.get(ch, 0) + 1

        heap = [(-cnt, ch) for ch, cnt in m.items()]
        heapify(heap)

        res = []
        prev = None

        while heap:
            cnt, ch = heappop(heap)
            res.append(ch)

            if prev:
                heappush(heap, prev)
                prev = None

            cnt += 1

            if cnt < 0:
                prev = (cnt, ch)

        return ''.join(res) if len(res) == len(s) else ''

