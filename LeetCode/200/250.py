class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_converter = {}
        t_converter = {}
        for sc, tc in zip(s, t):
            if sc not in s_converter and tc not in t_converter:
                s_converter[sc] = tc
                t_converter[tc] = sc
            else:
                if sc in s_converter:
                    if s_converter[sc] != tc:
                        return False
                else:
                    s_converter[sc] = tc

                if tc in t_converter and t_converter[tc] != sc:
                    if t_converter[tc] != sc:
                        return False
                else:
                    t_converter[tc] = sc
        return True

