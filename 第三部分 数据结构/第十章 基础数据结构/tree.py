# coding=utf-8
__author__ = 'PyBeaner'


class Node:
    def __init__(self, value):
        self.value = value
        self.root = None
        self.left_child = None
        self.right_sibling = None

    def __str__(self):
        return "Node(%s)" % (self.value,)


class Tree:
    def __init__(self, root=None):
        self.root = root

    # 深度遍历
    def __iter__(self):
        if self.root:
            yield self.root
            left_child = self.root.left_child
            if left_child:
                yield from Tree(left_child)
                right_sibling = left_child.right_sibling
                while right_sibling:
                    yield from Tree(right_sibling)
                    right_sibling = right_sibling.right_sibling

    def display(self):
        if not self.root:
            print("Tree End")
            return
        if not self.root.root:
            print(self.root)
        node = self.root.left_child
        while node:
            print(node, end=",")
            node = node.right_sibling
        print()
        left = self.root.left_child
        child_tree = Tree(left)
        child_tree.display()


def build_tree(root, width, height):
    if height <= 0:
        return
    for i in range(width):
        v = "{0} at height:{1}".format(i, height)
        node = Node(v)
        node.root = root
        node.right_sibling = None
        if not root.left_child:
            root.left_child = node
        else:
            right_sibling = root.left_child.right_sibling
            if right_sibling:
                while right_sibling.right_sibling:
                    right_sibling = right_sibling.right_sibling
            else:
                right_sibling = root.left_child
            right_sibling.right_sibling = node
        build_tree(node, width=width, height=height - 1)
    return Tree(root)


if __name__ == '__main__':
    root = Node("root")
    t = build_tree(root, 3, 3)
    # for node in t:
    #     print(node)
    t.display()