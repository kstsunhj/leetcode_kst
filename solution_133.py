"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        que = collections.deque()
        hashd = dict()
        que.append(node)
        node_copy = Node(node.val, [])
        hashd[node] = node_copy
        while que:
            t = que.popleft()
            if not t: continue
            for n in t.neighbors:
                if n not in hashd:
                    hashd[n] = Node(n.val, [])
                    que.append(n)
                hashd[t].neighbors.append(hashd[n])
        return node_copy
