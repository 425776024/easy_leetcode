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
    def swapPairs(self, head):
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev, p = dummyHead, head
        while p != None and p.next != None:
            # p后面，后面的后面
            q, r = p.next, p.next.next
            # p前面的与p后面的点连接
            prev.next = q
            # p后面的点与p连接，实现反转(1,2)
            q.next = p
            # p连到后2点，重新接回串上，以便下一次反转(3,4)
            p.next = r
            # prev一直是p前面一个节点
            prev = p
            p = r
        return dummyHead.next


head = Solution().swapPairs(make_list([1, 2, 3, 4]))
print_list(head)
