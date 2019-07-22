import re
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        s = re.split(' |,', str(paragraph))
        # print(s)
        s = map(lambda w: ''.join(filter(str.isalpha, list(str(w.lower())))), s)
        c = Counter(s)
        # print(c)
        for w, i in c.most_common():
            if len(w) > 0 and w not in banned:
                return w
