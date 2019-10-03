class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        wrap_x = max(min(G, C) - max(E, A), 0)
        wrap_y = max(min(D, H) - max(B, F), 0)
        print(wrap_x, wrap_y)
        rect1 = (C - A) * (D - B)
        rect2 = (G - E) * (H - F)
        print(rect1, rect2, wrap_x * wrap_y)
        return rect1 + rect2 - wrap_x * wrap_y
