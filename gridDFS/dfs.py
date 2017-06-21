class DirectedEdge(object):
    # Memory-saving hack; doesn't work for Node. Similar to a namedtuple.
    __slots__ = ('src', 'dest')

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

class Node(object):
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.edges = set()

    def add(self, node):
        """Add node to self, returning the new edge.

        This won't repeat neighbors, but ALWAYS creates a new edge!
        """
        self.neighbors.add(node)
        e = DirectedEdge(self, node)
        self.edges.add(e)
        return e

class DBGraph(object):
    """De Bruijn Graph data structure.

    Assume node labels to be distinct.
    Edges need not be distinct up to labels.
    """

    def __init__(self, V, E):
        self.nodes = {}
        # Assume labels to be distinct
        for label in set(V):
            node = Node(label)
            self.nodes[label] = node

        self.edges = set()
        for src, dest in E:
            src_node = self.nodes[src]
            dest_node = self.nodes[dest]
            edge = src_node.add(dest_node)
            self.edges.add(edge)

        # Use this to track your walk
        self.visited = set()
        # In case you need a stack for depth-first search
        # You'll want to add some additional methods for this...
        # ...e.g. def free_neighbors(self, node):
        self.stack = []

    def __str__(self):
        """Define this if you want to call str(graph) to print it for debugging.
        """
        pass

    def reset(self):
        """Just a clean, semantic interface to restart your walk.
        """
        self.visited = set()
        self.stack = []

    def walk(self):
        """YOUR ALGORITHM HERE
        """
        pass

if __name__ == '__main__':
    # Very contrived data set
    v = ['AG', 'GA', 'AC']
    e = [('AG', 'GA'), ('GA', 'AC'), ('GA', 'AG')]
    g = DBGraph(v, e)

    # Example usage of the interfaces
    for node in g.nodes.values():
        for n in node.neighbors:
            print(node.label, n.label)

    # Note that node.neighbors and node.edges are sets!
    # This means you can do something like this in your algorithm:
    # visited = set(...)
    # unvisited = n.neighbors.difference(visited)
