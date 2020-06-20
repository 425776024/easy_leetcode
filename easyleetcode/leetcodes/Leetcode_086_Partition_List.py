
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(arr: list):
    head_node = None
    p_node = None
    for a in arr:
        new_node = ListNode(a)
        if head_node is None:
            head_node = new_node
            p_node = new_node
        else:
            p_node.next = new_node
            p_node = new_node
    return head_node


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=',')
        head = head.next


class Solution:
    def partition(self, head, x):
        if head is None:
            return None
        # 左"串"头节点
        left_P = ListNode(0)
        # 左"串"尾节点
        left = left_P
        # 右"串"头节点
        right_P = ListNode(0)
        # 右"串"尾节点
        right = right_P
        # 原始串尾节点
        node = head

        while node is not None:
            # <x的串到left节点下
            # >=x的串到right节点下
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            node = node.next
        right.next = None
        left.next = right_P.next
        return left_P.next


s = Solution()
a = [1, 4, 3, 2, 5, 2]
head = make_list(a)
print_list(head)
head = s.partition(head, x=3)
print()
print_list(head)
