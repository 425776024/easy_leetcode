
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
    def insertionSortList(self, head):
        # 1.建立新的头节点
        dummy = ListNode(0)
        # 3.每次从原串中cur节点放入新串中合适位置，然后cur右移
        cur = head
        while cur is not None:
            # pre每次从头节点开始，找到插入位置
            pre = dummy
            # 2遍历新串：找到pre.next 比cur大，pre比cur小的位置，然后在pre后面插入
            while pre.next is not None and pre.next.val < cur.val:
                pre = pre.next
            temp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
        return dummy.next


head = make_list([1, 3, 2, 0])
print_list(head)
s = Solution()
head = s.insertionSortList(head)
print_list(head)
