
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
    def removeNthFromEnd(self, head: ListNode, n: int):
        pre = head
        cur = head
        for _ in range(n):
            cur = cur.next
        # 就2个，n=1
        if cur is None:
            return head.next
        # cur.next is None的时候，cur是最后一个node
        while cur.next is not None:
            cur = cur.next
            pre = pre.next
        # 穿过倒数第n个节点不要
        pre.next = pre.next.next
        return head


s = Solution()
a = [1, 2, 3, 4, 5]
head = make_list(a)
print_list(head)
print()
print_list(s.removeNthFromEnd(head, n=2))
