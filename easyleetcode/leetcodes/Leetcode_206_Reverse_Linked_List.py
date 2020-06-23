
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(arr):
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


def print_list(head):
    while head is not None:
        print(head.val, end=',')
        head = head.next


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # fix head
        head = prev

        return head



s = Solution()
a = [1, 2, 3, 4, 5]
head = make_list(a)
print_list(head)
r_head=s.reverseList(head)
print()
print_list(r_head)