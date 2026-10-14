class TimeMap:

    def __init__(self):
        self.kvStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kvStore:
            arr = self.kvStore[key]
            arr.append((timestamp, value)) 
        else:
            self.kvStore[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        if key not in self.kvStore:
            return res

        arr = self.kvStore[key]
        l,r=0,len(arr)-1
        while l<=r:
            mid = l + (r-l)//2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
