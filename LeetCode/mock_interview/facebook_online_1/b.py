class Solution:
    def customSortString(self, S, T):
        order = {}
        rev_order = {}
        li = list(S)
        for i in range(li):
            order[li[i]] = i
            rev_order[i] = li[i]

        print(order)
        can_order = list(filter(lambda x: x in order, T))
        can_not_order = list(filter(lambda x: x not in order, T))

        num_t = list(map(lambda x: order[x], can_order))
        num_t.sort()

        ordered = list(map(lambda x: rev_order[x], num_t))

        return order + can_not_order

