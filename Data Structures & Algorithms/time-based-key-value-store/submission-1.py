class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hm.get(key, None) is not None:
            self.hm[key].append({"value": value, "timestamp": timestamp})
        else:
            self.hm[key] = [{"value":value, "timestamp":timestamp}]

    def get(self, key: str, timestamp: int) -> str:
        if self.hm.get(key, None) is not None:
            lst = self.hm[key]
            l, r = 0, len(lst) - 1
            
            temp = lst[0]
            while l <= r:
                m = l + (r - l) // 2

                if lst[m]["timestamp"] <= timestamp:
                    if temp["timestamp"] < lst[m]["timestamp"]:
                        temp = lst[m]
                    l = m + 1
                elif lst[m]["timestamp"] > timestamp:
                    r = m - 1
            return temp["value"] if temp["timestamp"] <= timestamp else ""
            
        return ""

