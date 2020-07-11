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
    print()


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        pos = dummyHead = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        # merge residual l1
        if l1 is not None:
            pos.next = l1
        # merge residual l2
        if l2 is not None:
            pos.next = l2
        return dummyHead.next

s = Solution()

l1 = make_list([1, 3, 5])
print_list(l1)
l2 = make_list([2,4,6,8,10])
print_list(l2)

res=s.mergeTwoLists(l1,l2)
print_list(res)
