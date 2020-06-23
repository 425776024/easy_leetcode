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


class Solution_mergeTwoLists(object):
    def mergeTwoLists(self, l1, l2):
        pos = dummyHead = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        # merge residual l1
        if l1 is not None:
            pos.next = l1
        # merge residual l2
        if l2 is not None:
            pos.next = l2
        return dummyHead.next


class Solution(object):

    def mergeKLists(self, merge2Lists, K_list):
        head = K_list[0]
        for i in range(1, len(K_list)):
            head = merge2Lists(head, K_list[i])

        return head
    
    def mergeKLists2(self, merge2Lists, K_list):
        # 二分两两不同的合并，合并一轮了，再两两合并，直到只剩一条list
        # 递归函数helper：合并star <-> end的list:  
        	# start == end :return List[start]
            # start+1 == end :return merge2Lists(List[start],List[end])
            # left = helper(start, start + (end - start) / 2)
        	# right = helper(start + (end - start) / 2 + 1, end)
            # return merge2Lists(left,right)

        pass


s1 = Solution_mergeTwoLists()
s = Solution()
l1 = make_list([1, 3, 5])
l2 = make_list([2, 4, 6, 8, 10])
l3 = make_list([7, 8, 9, 11, 14])
K_list = [l1, l2, l3]

head = s.mergeKLists(s1.mergeTwoLists, K_list)
print_list(head)
