from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        calc_results = defaultdict(lambda: {})
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            calc_results[numerator][denominator] = values[i]
            calc_results[denominator][numerator] = 1 / values[i]
            calc_results[denominator][denominator] = 1
            calc_results[numerator][numerator] = 1

        def calc(n, d, path):
            # print('{} {} {}'.format(n,d, path))
            if n in calc_results and d in calc_results:
                if d in calc_results[n]:
                    return calc_results[n][d]
                else:
                    for candidate in calc_results[n]:
                        if candidate not in path:
                            val = calc(candidate, d, path + [candidate])
                            if val != -1:
                                return calc_results[n][candidate] * val
                    return -1
            else:
                return -1

        ans = []
        for q in queries:
            found = False
            n, d = q[0], q[1]
            ans.append(calc(n, d, [n]))

        return ans