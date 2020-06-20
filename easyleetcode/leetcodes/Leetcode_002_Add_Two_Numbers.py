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
    def two_list_sum(self, head1, head2):
        p = 0
        sumlist = ListNode(0)
        pre = sumlist
        # 长度可能不一样，只要有一个有值，就得继续
        while head1 is not None or head2 is not None:
            # 分3种情况讨论，1:都还有的时候
            if head1 is not None and head2 is not None:
                v = head1.val + head2.val + p
                head1 = head1.next
                head2 = head2.next
        # 2: 前者有，后者没有
            elif head1 is not None and head2 is None:
                v = head1.val + p
                head1 = head1.next
            else: # 3，后者有
                v = head2.val + p
                head2 = head2.next
            # 进位情况
            p = 0
            if v > 9:
                v = v - 10
                p = 1
            # 当前点值超过9进位，个位赋给v，进位到中p
            node = ListNode(v)
            pre.next = node
            pre = node
        # 最为关键，如果前面一步还能进位，不要了？
        if p == 1:
            node = ListNode(1)
            pre.next = node

        return sumlist


s = Solution()
a = [3, 1, 5]
a2 = [5, 9, 5, 9]
head1 = make_list(a)
head2 = make_list(a2)
print_list(head1)
print()
print_list(head2)
print()

# res_sum.next ? 不需要头节点的伪值
res_sum = s.two_list_sum(head1, head2).next
print_list(res_sum)
