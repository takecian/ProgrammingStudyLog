class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic = {}
        rev_dic = {}
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        for p, s in zip(pattern, str):
            # print('{} {}'.format(p, s))
            if p not in dic:
                if s in rev_dic:
                    return False
                dic[p] = s
                rev_dic[s] = p
            else:
                if dic[p] != s:
                    return False
        return True
