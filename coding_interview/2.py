# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 2.1

input_list = Node(
    val=1, next=(Node(val=1, next=Node(val=1, next=Node(val=2, next=None))))
)


def _compare_nodes(l1, l2):
    while l1 is not None:
        if l1.val == l2.val:
            l1, l2 = l1.next, l2.next
        else:
            return False

    return l1 is l2


def remove_dups(linked_list: Node) -> Node:

    head = linked_list
    seen = set()

    prev = None
    while linked_list is not None:

        if linked_list.val in seen:
            prev.next = linked_list.next
        else:
            prev = linked_list
            seen.add(linked_list.val)

        linked_list = linked_list.next

    return head


assert _compare_nodes(remove_dups(input_list), Node(val=1, next=Node(val=2, next=None)))

# 2.2

input_k_node = Node(
    val=8,
    next=(
        Node(
            val=7,
            next=Node(
                val=6,
                next=Node(
                    val=5,
                    next=Node(
                        val=4,
                        next=(
                            Node(val=3, next=Node(val=2, next=Node(val=1, next=None)))
                        ),
                    ),
                ),
            ),
        )
    ),
)


def find_k(n: Node, k: int) -> int:
    escaping = n

    for _ in range(k - 1):
        n = n.next
        if n is None:
            return -1

    while n.next is not None:
        escaping = escaping.next
        n = n.next

    return escaping.val


assert find_k(input_k_node, 3) == 3

GLOBAL_NODE: Node = None


def find_k_recursive(n: Node, k: int) -> int:

    if n is None:
        return 0

    count = find_k_recursive(n.next, k) + 1

    # print(count)

    if count == k:
        global GLOBAL_NODE
        GLOBAL_NODE = n

    return count


find_k_recursive(input_k_node, 6)
assert GLOBAL_NODE.val == 6


# 2.3


del_node = Node(val=3, next=Node(val=4, next=None))
input_2_3 = Node(val=1, next=(Node(val=2, next=del_node)))


def delete_middle_node(node):
    while True:
        node.val = node.next.val

        if node.next.next is None:
            node.next = None
            break

        node = node.next


delete_middle_node(del_node)
assert _compare_nodes(
    input_2_3,
    Node(val=1, next=(Node(val=2, next=Node(val=4, next=None)))),
)


# 2.4

input_partition = Node(
    val=3,
    next=(
        Node(
            val=5,
            next=Node(
                val=8,
                next=Node(
                    val=5,
                    next=Node(
                        val=10,
                        next=(Node(val=2, next=Node(val=1, next=None))),
                    ),
                ),
            ),
        )
    ),
)


def make_partition(node, partition):
    if node is None:
        return None

    head = node
    prev = node
    node = node.next

    while node is not None:
        if node.val < partition:
            prev.next = node.next
            node.next = head
            head = node
            node = prev.next
        else:
            prev = node
            node = node.next

    return head


assert _compare_nodes(
    make_partition(input_partition, 5),
    Node(
        val=1,
        next=(
            Node(
                val=2,
                next=Node(
                    val=3,
                    next=Node(
                        val=5,
                        next=Node(
                            val=8,
                            next=(Node(val=5, next=Node(val=10, next=None))),
                        ),
                    ),
                ),
            )
        ),
    ),
)


# 2.5


sum1 = Node(val=7, next=(Node(val=1, next=Node(val=6, next=None))))

sum2 = Node(val=5, next=(Node(val=9, next=Node(val=2, next=None))))


def node_sum(n1, n2):
    remainder = 0
    head, pointer = None, None

    while n1 is not None or n2 is not None:
        if n1 is None:
            n1 = Node(val=0, next=None)
        if n2 is None:
            n2 = Node(val=0, next=None)

        n_sum = n1.val + n2.val + remainder
        remainder, current = n_sum // 10, n_sum % 10

        current_node = Node(val=current, next=None)
        if head is None:
            head, pointer = current_node, current_node
        else:
            pointer.next = current_node
            pointer = current_node

        n1, n2 = n1.next, n2.next

    if remainder == 1:
        pointer.next = Node(val=1, next=None)

    return head


assert _compare_nodes(
    node_sum(sum1, sum2),
    Node(val=2, next=(Node(val=1, next=Node(val=9, next=None)))),
)
assert _compare_nodes(
    node_sum(Node(val=2, next=(Node(val=1, next=Node(val=9, next=None)))), Node(val=2, next=None)),
    Node(val=4, next=(Node(val=1, next=Node(val=9, next=None)))),
)

assert _compare_nodes(
    node_sum(Node(val=9, next=(Node(val=9, next=None))), Node(val=1, next=None)),
    Node(val=0, next=(Node(val=0, next=Node(val=1, next=None)))),
)

# 2.5 reverse

sum1 = Node(val=6, next=(Node(val=1, next=Node(val=7, next=None))))

sum2 = Node(val=2, next=(Node(val=9, next=Node(val=5, next=None))))


def node_sum_reverse(n1, n2):
    n1 = reverse(n1)
    n2 = reverse(n2)
    s = node_sum(n1, n2)
    return reverse(s)


def reverse(n):

    if n is None:
        return None

    return Node(val=n.val, next=reverse(n.next))


sum1_rec = Node(val=6, next=(Node(val=1, next=Node(val=7, next=None))))

sum2_rec = Node(val=2, next=(Node(val=9, next=Node(val=5, next=None))))

from dataclasses import dataclass


@dataclass
class SumNode:
    sum: Node = None
    carry: int = 0


def node_sum_rec(n1, n2):

    make_len_eq(n1, n2)

    sum_node = sum_rec(n1, n2)

    # + обработка кейса если осталось carry

    return sum_node.sum




def make_len_eq(n1, n2):
    pass

def sum_rec(n1, n2):

    if n1 is None:
        return SumNode()

    sum_node = sum_rec(n1.next, n2.next)

    val = n1.val + n2.val + sum_node.carry
    sum_val, carry = val%10, val//10

    node = Node(val=sum_val, next=sum_node.sum)

    return SumNode(node, carry)



assert _compare_nodes(
    node_sum_rec(sum1, sum2),
    Node(val=9, next=(Node(val=1, next=Node(val=2, next=None)))),
)


# 2.6

p_node = Node(val=7, next=(Node(val=1, next=Node(val=7, next=None))))


def check_palindrome(node):

    length = get_len(node)
    stack = check_palindrome_rec(Stack(node=node,is_palindrome=True), length=length)
    return stack.is_palindrome


@dataclass
class Stack:
    node: Node
    is_palindrome: bool = True


def check_palindrome_rec(node: Stack, length):

    if length == 0: # четное
        return Stack(node=node.node)
    if length == 1:  # нечетное
        # node.next - центр, его пропускаем и берем следующую ноду
        return Stack(node=node.node.next)

    length = length-2
    front_node = node.node
    stack = check_palindrome_rec(Stack(node=front_node.next), length)
    reversed_node = stack.node
    is_palindrome = stack.is_palindrome and (front_node.val==reversed_node.val)
    return Stack(node=reversed_node.next, is_palindrome=is_palindrome)



def get_len(node):
    counter = 0
    while node is not None:
        counter += 1
        node = node.next

    return counter


assert check_palindrome(p_node) is True
not_palindrome  = Node(val=7, next=(Node(val=1, next=Node(val=3, next=None))))
assert check_palindrome(not_palindrome) is False
palindrome  = Node(val=7, next=(Node(val=2, next=Node(val=2, next=Node(val=7, next=None)))))
assert check_palindrome(palindrome) is True




# 2.7

p_node_intersect = Node(val=7, next=(Node(val=1, next=None)))


p_node_1 = Node(val=7, next=p_node_intersect)
p_node_2 = Node(val=7, next=Node(val=7, next=Node(val=7, next=p_node_intersect)))


def find_intersection(n1, n2):
    len_n1, tail1 = find_len_and_tail(n1)
    len_n2, tail2 = find_len_and_tail(n2)

    if tail1 != tail2:
        return

    if len_n1 > len_n2:
        for _ in range(len_n1-len_n2):
            n1 = n1.next

    if len_n2 > len_n1:
        for _ in range(len_n2-len_n1):
            n2 = n2.next

    for _ in range(min(len_n1,len_n2)):
        if n1 == n2:
            return n1

        n1 = n1.next
        n2 = n2.next

    return None


def find_len_and_tail(n):
    if n is None:
        return 0

    counter = 1
    while n.next is not None:
        counter += 1
        n = n.next

    return counter, n


assert find_intersection(p_node_1,p_node_2) == p_node_intersect
assert find_intersection(p_node_1,p_node) is None


# 2.8

_loop = Node(val=5, next=None)
_p_node_loop = Node(val=2, next=Node(val=3, next=Node(val=4, next=_loop)))
_loop.next = _p_node_loop

p_node_loop = Node(val=1, next=Node(val=10, next=_p_node_loop))


# _loop = Node(val=3, next=None)
# _p_node_loop = Node(val=2, next=_loop)
# _loop.next = _p_node_loop
#
# p_node_loop = Node(val=1, next=_p_node_loop)


def detect_loop(n):
    if n is None or n.next is None:
        return None

    slow_pointer = n
    fast_pointer = n.next

    while slow_pointer != fast_pointer:
        if fast_pointer is None or fast_pointer.next is None:
            return None

        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    print(f"collision on {slow_pointer.val}, {fast_pointer.val}")


    slow_pointer = n
    fast_pointer = fast_pointer.next
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer

print(detect_loop(p_node_loop).val)





