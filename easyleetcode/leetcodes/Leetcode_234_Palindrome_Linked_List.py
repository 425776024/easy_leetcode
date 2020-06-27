
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
    def is_palindrome(self, head):
        if not head or not head.next:
            return True
        # slow到中点前
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 中点
        mid = slow.next
        # [1, 3, 4, 3, 1] mid:3 
        # [1, 3, 4, 5, 3, 1] mid:5
        # 打断前、后段
        slow.next = None
        # 反转后半段
        rhead = self.reverse(mid)
        # 奇数时len(rhead) = len(head) -1
        # 偶数时len(rhead) = len(head)
        # 所以，得拿rhead遍历，这样奇数个时，最后留下head最后一个值，不比较也可以。
        # 否则拿head遍历，多出的没得比较，会出错
        while rhead:
            if rhead.val != head.val:
                return False
            rhead = rhead.next
            head = head.next
        return True

    def reverse(self, head):
        dummy = ListNode(-1)
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
        return dummy.next


head = make_list([1, 3, 4,3, 1])
print_list(head)
s = Solution()
head = s.is_palindrome(head)
print(head)


head = make_list([1, 3, 4, 4, 3, 1])
print_list(head)
s = Solution()
head = s.is_palindrome(head)
print(head)