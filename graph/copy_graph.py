class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(self, node: Node) -> Node:
    if node is None:
        return node
    nodes = {}

    stack = [node]
    nodes[node] = Node(node.val)
    while stack:
        current = stack.pop()
        for neighbor in current.neighbors:
            if neighbor not in nodes:
                stack.append(neighbor)
                nodes[neighbor] = Node(neighbor.val)
            nodes[current].neighbors.append(nodes[neighbor])
    return nodes[node]