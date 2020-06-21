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
    def deleteDuplicates(self, head):
        if head is None:
            return None

        curr = head
        while curr is not None:
            inner = curr
            while inner.next is not None:
                if inner.next.val == curr.val:
                    inner.next = inner.next.next
                else:
                    inner = inner.next
            curr = curr.next

        return head

    def deleteDuplicates_hash(self, head):
        if head is None:
            return None

        hash = {}
        hash[head.val] = True
        curr = head
        while curr.next is not None:
            # 在，则曾经被加入了，此值需要被跳过
            if curr.next.val in hash:
                curr.next = curr.next.next
            else:
                hash[curr.next.val] = True
                curr = curr.next

        return head



s = Solution()
a = [12, 11, 12, 21, 41, 43, 21]
head = make_list(a)
print_list(head)

# 题解1 - 2个for
# head = s.deleteDuplicates(head)

# 题解2 - 万能的 hashtable
head = s.deleteDuplicates_hash(head)
print()
print_list(head)

