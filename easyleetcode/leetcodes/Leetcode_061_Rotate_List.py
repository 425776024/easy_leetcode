
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


class Solution:
    def rotateRight(self, head, k):
        '''
        先遍历整个链表获得链表长度n，然后此时把链表头和尾链接起来，在往后走n - k % n个节点就到达新链表的头结点前一个点，这时断开链表即可
        :param head:
        :param k:
        :return:
        '''
        if not head:
            return None
        # 链表长度n
        n = 1
        cur = head
        # cur到最后一个节点
        while cur.next:
            n += 1
            cur = cur.next
        # 最后一个节点与第一个节点连接
        cur.next = head
        # 继续走n - k % n个位置，就是满足要求串，的头结点的前一个点
        m = n - k % n
        for i in range(m):
            cur = cur.next
        # 新的
        newhead = cur.next
        # 断开
        cur.next = None
        return newhead


head = make_list([1, 2, 3, 4, 5])
print_list(head)
head = Solution().rotateRight(head, 2)
print_list(head)
