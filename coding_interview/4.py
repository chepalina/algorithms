# 4.2

binary_search_array = [2, 4, 6, 8, 10, 20]

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:

    value: int
    children: Optional[list] = None


expected = Node(
    value=8,
    children=[
        Node(value=4, children=[Node(value=2), Node(value=6)]),
        Node(value=10, children=[None, Node(value=20)]),
    ],
)


def minimal_tree(array: list):

    if not array:
        return None

    if len(array) == 1:
        return Node(value=array[0])

    middle = len(array) // 2

    return Node(
        value=array[middle],
        children=[minimal_tree(array[0:middle]), minimal_tree(array[middle + 1 :])],
    )


# print(binary_search_array[0:3], "-", binary_search_array[3], "-", binary_search_array[3+1:])

# print(minimal_tree(binary_search_array))


# 4.3

input_tree = Node(
    value=8,
    children=[
        Node(value=4, children=[Node(value=2), Node(value=6)]),
        Node(value=10, children=[None, Node(value=20)]),
    ],
)


def create_arrays(tree: Node) -> list[list[int]]:
    line = [tree]
    target = []

    while line:
        _children = []
        _values = []
        for node in line:
            if node is not None:
                _values.append(node.value)
                _children.extend(node.children or [])

        line = _children
        target.append(_values)

    return target


# print(create_arrays(input_tree))


@dataclass
class NodeLR:

    value: int
    left: Optional["NodeLR"] = None
    right: Optional["NodeLR"] = None

    def __repr__(self):
        return str(self.value)


tree_43 = NodeLR(value=10, left=NodeLR(value=5), right=NodeLR(value=15))


# depth-first
def create_arrays_1(root_node: NodeLR):
    lists = []

    recursive_create_arrays(root_node, lists, 0)

    return lists


def recursive_create_arrays(node, lists, level):

    if node is None:
        return

    # define list
    if len(lists) == level:
        current_level_list = []
        lists.append(current_level_list)
    else:
        current_level_list = lists[level]

    current_level_list.append(node)

    recursive_create_arrays(node.left, lists, level + 1)
    recursive_create_arrays(node.right, lists, level + 1)


# print(create_arrays_1(tree_43))


# breadth-first
def create_arrays_breadth(root_node):
    lists = []

    if root_node is None:
        return []

    prev = [root_node]

    while prev:
        lists.append(prev)
        current = []

        for node in prev:

            if node.right is not None:
                current.append(node.right)

            if node.left is not None:
                current.append(node.left)

        prev = current

    return lists


# print(create_arrays_breadth(tree_43))


# 4.4


@dataclass
class Node4_4:

    value: int
    left: Optional["Node4_4"] = None
    right: Optional["Node4_4"] = None

    def __repr__(self):
        return str(self.value)


def main_check_balanced(node: Node4_4):
    return check_balanced(node) < 2


def check_balanced(node: Node4_4):

    if node.right is None and node.left is None:
        return 0

    if node.left is not None:
        return check_balanced(node.left) + 1

    if node.right is not None:
        return check_balanced(node.right) + 1

    return max(check_balanced(node.left), check_balanced(node.right))


tree_44 = Node4_4(value=10, left=Node4_4(value=5), right=Node4_4(value=15))

# assert check_balanced(tree_44) is True


tree_44_f = Node4_4(
    value=10,
    left=Node4_4(value=5),
    right=Node4_4(value=15, right=Node4_4(value=16, right=Node4_4(value=17))),
)

# assert check_balanced(tree_44) is False


# 4.5

tree_45_true = Node4_4(
    value=8,
    left=Node4_4(value=4, left=Node4_4(value=2), right=Node4_4(value=6)),
    right=Node4_4(value=10, right=Node4_4(value=20)),
)
tree_45_false = Node4_4(
    value=8,
    left=Node4_4(value=4, left=Node4_4(value=2), right=Node4_4(value=12)),
    right=Node4_4(value=10, right=Node4_4(value=20)),
)
tree_45_false_2 = Node4_4(
    value=8,
    left=Node4_4(value=4, left=Node4_4(value=2), right=Node4_4(value=6)),
    right=Node4_4(value=100, right=Node4_4(value=20)),
)


import sys

MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize


def validate_bst(root: Node4_4) -> bool:
    def check_boarders(min_value, max_value, node) -> bool:

        if not node.left and not node.right:
            return min_value <= node.value < max_value

        left_node_valid = True
        right_node_valid = True

        if node.left:
            left_node_valid = (node.value >= min_value) and check_boarders(
                min_value, node.value, node.left
            )

        if node.right:
            right_node_valid = (node.value < max_value) and check_boarders(
                node.value + 1, max_value, node.right
            )

        return left_node_valid and right_node_valid

    return check_boarders(MIN_INT, MAX_INT, root)


# print(validate_bst(tree_45_false))
assert validate_bst(tree_45_true) is True
assert validate_bst(tree_45_false) is False
assert validate_bst(tree_45_false_2) is False

# 4.6


@dataclass
class Node46:

    value: int
    left: Optional["Node46"] = None
    right: Optional["Node46"] = None
    parent: Optional["Node46"] = None

    def __repr__(self):
        return str(self.value)


left = Node46(value=5)
right = Node46(value=20)
first_node = Node46(value=10, left=left, right=right)
left.parent = first_node
right.parent = first_node

left.left = Node46(value=2, parent=left)
left.right = Node46(value=7, parent=left)

right.left = Node46(value=15, parent=right)
last = Node46(value=30, parent=right)
right.right = last

tree_46 = first_node


def inorder(node: Node46):
    """Алгоритм in-order traversal"""

    if node is None:
        return

    inorder(node.left)
    print(node)
    inorder(node.right)


# inorder(tree_46)


def successor(node: Node46) -> Optional[Node46]:
    if not node:
        return

    if node.right:
        return get_leftmost(node.right)

    parent = node.parent

    while parent is not None:

        if node == parent.left:
            return parent

        node = parent
        parent = node.parent

    # дошли до верхней ноды, возможно только из самой правой ноды
    return None


def get_leftmost(node: Node46) -> Node46:

    while node.left is not None:
        node = node.left

    return node


# print(successor(tree_46)) # 15
# print(successor(last)) # None
# print(successor(left.left)) # 5


# --------------------------------------------------
# Геренератор inorder обхода.
# Сложность Time O(N).
# Space O(H). *H - высота дерева.
# --------------------------------------------------


def inorder_gen(root):
    if root:
        yield from inorder_gen(root.left)
        yield root
        yield from inorder_gen(root.right)


gen = inorder_gen(tree_46)

# print(next(gen))
#
# for i in inorder_gen(tree_46):
#     print(i)

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------


# 4.7 Build projects

projects_input = ["a", "b", "c", "d", "e", "f"]
dependencies_input = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]


class Graph:
    def __init__(self):
        self.map = {}

    def __repr__(self):
        return str(self.map.values())

    def add_node(self, name: str):
        self.map[name] = NodeProject(name)

    def add_edge(self, node_a, node_b):
        first = self.map.get(node_a)
        second = self.map.get(node_b)
        first.add_child(second)

    def size(self):
        return len(self.map)


class NodeProject:
    def __init__(self, name: str):
        self.name = name
        self.map = {}
        self.children = []
        self.dependencies_count = 0

    def __repr__(self):
        return f"{self.name}:{self.dependencies_count} ({self.map.keys()})"

    def add_child(self, node):
        if not self.map.get(node.name):
            self.map[node.name] = node
            self.children.append(node)
            node.increment()

    def increment(self):
        self.dependencies_count += 1

    def decrement(self):
        self.dependencies_count -= 1


def build_order(projects: list[str], dependencies: list[tuple[str, str]]) -> list[str]:

    graph = build_graph(projects, dependencies)

    order = order_projects(graph)

    print([o.name for o in order])


def build_graph(projects, dependencies):
    graph = Graph()

    for p in projects:
        graph.add_node(p)

    for d in dependencies:
        graph.add_edge(*d)

    return graph


def order_projects(graph):
    result = [None] * graph.size()

    projects = graph.map.values()

    end = get_non_dependent(result, projects, offset=0)

    processing = 0
    while processing < graph.size():
        current = result[processing]

        if current is None:
            return None

        for c in current.children:
            c.decrement()

        end = get_non_dependent(result, current.children, offset=end)
        processing += 1

    print(result)
    return result


def get_non_dependent(result, projects, offset):
    print(offset)

    for p in projects:
        if p.dependencies_count == 0:
            result[offset] = p
            offset += 1

    return offset


# build_order(projects_input,dependencies_input)


# 4.8 Common ancestor


@dataclass
class Node48:

    value: int
    left: Optional["Node48"] = None
    right: Optional["Node48"] = None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


tree_48 = Node48(
    value=3, left=Node48(value=1), right=Node48(value=5, left=Node48(6), right=Node48(value=8))
)


tree_48_small = Node48(
    value=3, left=Node48(value=1), right=Node48(value=5))


def common_ancestor(root: "Node48", p: "Node48", q: "Node48"):

    if root is None:
        return None

    if p == root and q == root:
        return root

    left = common_ancestor(root.left, p, q)
    print(f"common_ancestor left({root.left, p, q}) -- {root}, {left=}")

    # already found ancestor
    if left is not None and left != p and left != q:
        return left

    right = common_ancestor(root.right, p, q)
    print(f"common_ancestor right({root.right, p, q}) -- {root}, {right=}")

    # already found ancestor
    if right is not None and right != p and right != q:
        print("Already found right")
        return right

    # p and q in diff subtrees -> root is common
    if left is not None and right is not None:
        print("Main result")
        return root

    if root == p or root == q:
        return root

    return right or left


print(common_ancestor(tree_48, Node48(6), Node48(8)))
# print(common_ancestor(tree_48_small, Node48(1), Node48(5)))


# 4.9 BST Sequence

tree_49 = NodeLR(
    value=2, left=NodeLR(value=1), right=NodeLR(value=3))

tree_49_big = NodeLR(
    value=50, left=NodeLR(value=20, right=NodeLR(value=25)), right=NodeLR(value=60, right=NodeLR(value=70)))


result49 = []


#  4.9 sub problem - two list combinations

list1 = [1,2]
list2 = [3,4]


def weave(first: list, second: list, results: list, prefix: list):

    if not first or not second:
        result = prefix + first + second
        results.append(result)
        return

    # first list
    first_head = first.pop(0)
    prefix.append(first_head)

    weave(first, second, results, prefix)

    prefix.pop()
    first.insert(0, first_head)

    # second list
    second_head = second.pop(0)
    prefix.append(second_head)

    weave(first, second, results, prefix)

    prefix.pop()
    second.insert(0, second_head)


# results49 = []
#
# weave(list1,list2,results49, [])
#
# print(results49)

def all_seq(root: "NodeLR"):

    result = []

    if root is None:
        result.append([])
        return result

    prefix = [root.value]

    left_seq = all_seq(root.left)
    right_seq = all_seq(root.right)

    # weave
    for l in left_seq:
        for r in right_seq:
            weaved = []
            weave(l, r, weaved, prefix)
            result.extend(weaved)

    return result


r = all_seq(tree_49_big)
print(r)


# 4.10 check_subtree()


t1_4_10 = NodeLR(
    value=2, left=NodeLR(value=1), right=NodeLR(value=3))

t2_4_10 = NodeLR(value=1)



def check_subtree(t1: NodeLR, t2: NodeLR):

    if not t1 or not t2:
        return False

    l1 = []
    get_preorder(t1, l1)
    l2 = []
    get_preorder(t2, l2)

    print(l1, l2)

    s1 = ''.join(l1)
    s2 = ''.join(l2)
    return s2 in s1


def get_preorder(t: NodeLR, l: list):

    if t is None:
        l.append(str(None))
        return

    l.append(str(t.value))
    get_preorder(t.right, l)
    get_preorder(t.left, l)



assert check_subtree(t1_4_10, t2_4_10) is True

