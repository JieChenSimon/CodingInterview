#把一个单链表打印出来 2025-11-15
#先这个程序的思路流程

#1. 实例化一个链表对象-主函数中-需要新建一个类，
#2. 向链表中添加节点 - 主函数-使用默认ListNode类
#3. 遍历链表并打印每个节点的值- 在新的类中包含打印函数

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):

        curr = self.head
        result = []
        # 遍历列表
        print('hi')
        while curr:
            tmp = curr.val
            print("tmp:", tmp)
            result.append(tmp)
            curr = curr.next
        print("The ListNode is", result)



if __name__ == "___main__":
    print('1')
    myLinkedList = MyLinkedList()

    #往里面添加节点
    myLinkedList.head = ListNode(1)
    myLinkedList.head.next = ListNode(2)
    print('i')

    myLinkedList.printList()







