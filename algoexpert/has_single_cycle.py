def hasSingleCycle(array):
    # Write your code here.
    length = len(array)
    visited = set()
    index = 0
    while True:
        if index in visited:
            if len(visited) == length and index == 0:
                return True
            else:
                return False
        visited.add(index)
        index = index + array[index]
        index = (index + length) % length
