# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class TimeMap:

    def __init__(self):
        self.s = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s.append([key, value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.s) - 1
        record = []

        while left <= right:
            mid = left + (right - left) // 2

            if self.s[mid][0] == key:
                record = self.s[mid]

                if self.s[mid][2] == timestamp:
                    return self.s[mid][1]
                elif self.s[mid][2] < timestamp:
                    record = self.s[left]
                    left = mid + 1
                else:
                    record = self.s[right]
                    right = mid - 1

        if record == []:
            return ""

        return record[1]


class TimeMapOptimized:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        res = ""
        values = self.store[key]
        
        left = 0
        right = len(values) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if values[mid][0] <= timestamp:
                # This timestamp is valid! Save the value.
                res = values[mid][1]
                # Try to find a CLOSER, larger valid timestamp to the right
                left = mid + 1
            else:
                # The timestamp is too large, search the left half
                right = mid - 1
                
        return res