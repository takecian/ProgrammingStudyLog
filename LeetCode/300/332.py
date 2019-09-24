class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        routes = collections.defaultdict(list)
        for fr, to in tickets:
            routes[fr].append(to)
        for fr in routes.keys():
            routes[fr].sort()

        stack = ['JFK']

        def dfs(fr):
            if len(stack) == n + 1:
                return stack
            dests = sorted(routes[fr])
            for dst in dests:
                stack.append(dst)
                routes[fr].remove(dst)
                can_go = dfs(dst)
                if can_go:
                    return stack
                stack.pop()
                routes[fr].append(dst)
            return None

        return dfs('JFK')