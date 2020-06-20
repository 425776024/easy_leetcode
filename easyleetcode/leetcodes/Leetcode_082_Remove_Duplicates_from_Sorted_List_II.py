
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
        # 指向头节点
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        # 有下一个，下下一个的时候，进行对比
        while node.next is not None and node.next.next is not None:
            # 如果下一个==下下一个的值，此值的全部要删，记录下
            if node.next.val == node.next.next.val:
                # 记录这个值
                val_prev = node.next.val
                # 凡是这个值的，pass，node.next=有这值的next
                while node.next is not None and node.next.val == val_prev:
                    node.next = node.next.next
            else:
                # 因为排序了，下一个和自己不想等，则一定是需要保留的
                node = node.next
        return dummy.next


s = Solution()
a = [1, 2, 3, 3, 4, 4, 5]
head = make_list(a)
print_list(head)
head = s.deleteDuplicates(head)
print()
print_list(head)
