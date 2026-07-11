class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            arr = self.mp[key]
            arr.append([value, timestamp])
        else:
            self.mp[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mp:
            return ''

        arr = self.mp[key]

        l,r = 0,len(arr)-1


        while l<=r:
            mid = l + (r-l)//2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return arr[r][0] if r >=0 else ''
