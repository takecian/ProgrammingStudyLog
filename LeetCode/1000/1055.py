import bisect


class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        if len(target) == 0:
            return 0

        lss = []
        j = 0
        for i, s in enumerate(source):
            if j < len(target) and s == target[j]:
                lss.append(i)
                j += 1

        if len(lss) == 0:
            return -1

        subs = ''.join(map(lambda i: source[i], lss))
        # print(subs)

        new_target = target[target.find(subs) + len(subs):]

        rest = self.shortestWay(source, new_target)
        if rest == -1:
            return -1
        else:
            return 1 + rest