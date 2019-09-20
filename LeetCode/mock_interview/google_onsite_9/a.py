class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_mapping = {}
        t_mapping = {}
        for sc, tc in zip(s, t):
            if sc not in s_mapping and tc not in t_mapping:
                s_mapping[sc] = tc
                t_mapping[tc] = sc
            else:
                if sc in s_mapping and s_mapping[sc] != tc:
                    return False
                if tc in t_mapping and t_mapping[tc] != sc:
                    return False
        return True
