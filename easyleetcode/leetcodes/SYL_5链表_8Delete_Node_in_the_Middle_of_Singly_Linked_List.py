

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
    def deleteNode(self, node):
        if node == None: return None
        if node.next == None: node = None

        node.val = node.next.val
        node.next = node.next.next


head = make_list([1, 3, 4, 5, 7, 9, 111])
print_list(head)
s = Solution()
# del 5
node = head.next.next.next
s.deleteNode(node)
print_list(head)
