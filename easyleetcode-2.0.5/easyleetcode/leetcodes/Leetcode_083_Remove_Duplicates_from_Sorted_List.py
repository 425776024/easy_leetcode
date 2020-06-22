

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
    def deleteDuplicates(self, head):
        if head is None:
            return None

        node = head
        while node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head


s = Solution()
a = [1, 1, 2, 3, 4, 4, 5]
head = make_list(a)
print_list(head)
head = s.deleteDuplicates(head)
print()
print_list(head)
