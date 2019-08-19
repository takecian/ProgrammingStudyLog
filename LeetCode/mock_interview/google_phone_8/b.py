import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_id += 1
        pos = bisect.bisect(self.array[index], [snap_id]) - 1
        return self.array[index][pos][1]
