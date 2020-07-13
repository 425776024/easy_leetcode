def make_list(arr):
    head_node = None
    p_node = None
    for a in arr:
        new_node = RandomListNode(a)
        if head_node is None:
            head_node = new_node
            p_node = new_node
        else:
            p_node.next = new_node
            p_node = new_node
    return head_node


def print_list(head):
    while head is not None:
        print(head.label, end=',')
        head = head.next
    print()


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        curNode = dummy
        randomMap = {}
        # copy list , 此时 拷贝后节点的random pointer指向的还是原来的节点，并没有完全拷贝出来
        while head is not None:
            # link newNode to new List
            newNode = RandomListNode(head.label)
            curNode.next = newNode
            # map old node head to newNode
            randomMap[head] = newNode
            # copy old node random pointer,拷贝旧链表中的 random 指针
            newNode.random = head.random
            head = head.next
            curNode = curNode.next

        # copy random
        curNode = dummy.next
        while curNode is not None:
            if curNode.random is not None:
                # 右边，curNode.random是原来list中的node
                # randomMap[curNode.random] 是list中的node的独自拷贝
                # 更新新链表中的 random 指针
                curNode.random = randomMap[curNode.random]
            curNode = curNode.next

        return dummy.next

    def copyRandomList2(self, head):
        dummy = RandomListNode(0)
        curNode = dummy
        hash_map = {}

        while head is not None:
            # link newNode to new List
            if head in hash_map.keys():
                newNode = hash_map[head]
            else:
                newNode = RandomListNode(head.label)
            curNode.next = newNode
            # map old node head to newNode
            hash_map[head] = newNode
            # copy old node random pointer
            if head.random is not None:
                if head.random in hash_map.keys():
                    newNode.random = hash_map[head.random]
                else:
                    # 这样下一到random的地方，就不会创建newNode，而是返回曾经创建好的hash_map[head.random]
                    newNode.random = RandomListNode(head.random.label)
                    hash_map[head.random] = newNode.random
            #
            head = head.next
            curNode = curNode.next

        return dummy.next


head = make_list([1, 2, 3, 4])
# 1->3
head.random = head.next.next
print_list(head)
s = Solution()
copy_head = s.copyRandomList2(head)
print_list(copy_head)
print(copy_head.random.label)
