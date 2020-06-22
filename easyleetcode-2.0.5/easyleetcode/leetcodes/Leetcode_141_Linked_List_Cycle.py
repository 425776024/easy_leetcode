

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
    def hasCycle(self, head: ListNode):
        slow = head
        fast = head
        # 无环，迟早退出
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            # 有环，迟早遇到，返回True
            if slow == fast:
                return True
        return False


s = Solution()
a = [1, 2, 3, 4, 5]
head = make_list(a)
# 造环
head.next.next.next.next.next = head.next.next
# 不能打印，死循环！@
# print_list(head)
print(s.hasCycle(head))
