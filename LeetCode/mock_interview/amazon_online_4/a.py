class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        key = { v: i for i, v, in enumerate(arr2) }
        in_arr1 = list(filter(lambda a: a in arr2, arr1))
        not_in_arr1 = list(filter(lambda a: a not in arr2, arr1))
        in_arr1.sort(key=lambda a: key[a])
        not_in_arr1.sort()
        return in_arr1 + not_in_arr1