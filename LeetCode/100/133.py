class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        edges = collections.defaultdict(list)

        dones = set()
        stack = [node]
        while stack:
            loop_node = stack.pop()
            if loop_node.val in dones:
                continue
            for neighbor in loop_node.neighbors:
                edges[loop_node.val].append(neighbor.val)
                stack.append(neighbor)
            dones.add(loop_node.val)

        # print(edges)
        if len(edges) > 0:
            node_dic = {}
            for val in edges.keys():
                node_dic[val] = Node(val, [])

            for key in edges.keys():
                for dst in edges[key]:
                    node_dic[key].neighbors.append(node_dic[dst])

            return node_dic[node.val]

        else:
            return Node(node.val, [])