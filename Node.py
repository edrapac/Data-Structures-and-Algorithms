class Node:

    def __init__(self, content, next_node=None, name=None):
        self.content = content
        self.next_node = next_node

        self.name = name

    def __repr__(self):  # this is mainly for ease of use so we can just print a node and get its
        # content without having to explicitly call methods
        return self.name