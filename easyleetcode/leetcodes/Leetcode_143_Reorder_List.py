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

    def reorderList(self, head):
        # Two points
        if head is None or head.next is None:
            return
        # 为了找到 中 节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            # two step
            fast = fast.next.next
        print(slow.val)
        # 退出while，fast是最后一个节点，或者None,slow 到中间
        last = slow.next
        slow.next = None

        # last的前方节点
        last_pre = None
        # reverse last:fast , 此后，从pre开始->next遍历，是从大到小
        while last:
            next = last.next
            last.next = last_pre
            last_pre = last
            last = next
        # 退出
        pre = last_pre
        # head开始next是从小到大
        while head and pre:
            # 从小到大的数据的下一个
            head_next = head.next
            # 从大到小的数据的下一个
            pre_next = pre.next
            # 从小到大的数据，和从大到小的数据，串起来
            head.next = pre
            pre.next = head_next
            # 到他们下一个点
            pre = pre_next
            head = head_next


a = [1, 2, 3, 4,5]
head = make_list(a)
s = Solution()
print_list(head)
s.reorderList(head)
print_list(head)
