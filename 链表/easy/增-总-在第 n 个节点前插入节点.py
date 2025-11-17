class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, index: int, val: int):
        if index < 0 or index > self.size:
            return -1
        
        #在头节点前加
        if index == 0:
            newNode = ListNode(val)
            # 把新的节点指向头节点
            newNode.next = self.head
            #把新的节点作为头节点
            self.head = newNode
            self.size += 1
            return 
        
        curr = self.head
        # 开始根据根据index进行遍历到index -1的位置，即index所代表的节点前节点
        for i in range(index - 1):
            curr = curr.next
        
        newNode = ListNode(val)
        newNode.next = curr.next
        curr.next = newNode
        self.size += 1



if __name__ == "__main__":
    # 实例化一个链表
    myLinkedList = MyLinkedList()

    # 建立一个基础链表，加值
    myLinkedList.head = ListNode(1)
    myLinkedList.head.next = ListNode(2)
    myLinkedList.head.next.next = ListNode(3)
    myLinkedList.size = 3

    n = 3
    # 进行在n节点前插入节点，值为val,如在第二个节点前加
    index_id = n - 1
    myLinkedList.addNode(index = index_id, val = 100)
    print(myLinkedList.head.val)
    print(myLinkedList.head.next.val)
    print(myLinkedList.head.next.next.val)
    print(myLinkedList.head.next.next.next.val)
    print("self.size", myLinkedList.size)

