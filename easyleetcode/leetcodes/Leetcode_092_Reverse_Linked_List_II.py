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
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head, m, n):
        # 指向头节点
        dummy = ListNode(0)
        dummy.next = head
        # 指到m-1点
        node = dummy
        for i in range(m-1):
            if node == None:
                return None
            else:
                node = node.next
        # 指到m-1点
        premNode = node
        # 指到m点
        mNode = node.next
        # 反转后，这是反转段最后一个点
        nNode = mNode
        # 当前反转操作节点
        postnNode = nNode.next
        for i in range(n-m):
            if postnNode == None:
                return None
            # 保存当前反转操作节点的下一个节点
            temp = postnNode.next
            # 当前反转操作节点，进行反转，指向前一个点
            postnNode.next = nNode
            # 前一个点前进一位，到当前点
            nNode = postnNode
            # 当前点前进一位，到当前点曾经的下一个点：postnNode.next
            postnNode = temp
        
        # premNode是点m-1节点，反转段完成后，需要指向反转串的第一个点（曾经反转串的最后一个点）（新的m节点）。
        premNode.next = nNode
        
        # 当退出range(n-m)时，postnNode：是到反转段 “外面去了”（曾经反转串的最后一个点的下一个点）。
        # 反转段最后一个点（曾经的第一个点），需要指向 postnNode
        mNode.next = postnNode

        return dummy.next


s = Solution()
a = [1, 2, 3, 4, 5]
head = make_list(a)
print_list(head)
r_head = s.reverseList(head, 2, 4)
print()
print_list(r_head)
