# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 03:48:25 2021

@author: rashi
"""

from linkedList import Node, LinkedList

list = LinkedList()

list.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")

list.head.next = tuesday
tuesday.next = wednesday
# print(list.head.next.data)


list.printList()
list.push("Yakshanba")



# list.insertAfter(list.head.next.next, "Seshanba kechasi")
# print(list.printList())

print(list.head.data)

list.append("Payshanba")
list.append("Juma")
print(list.printList())

list.deleteNode(2)
print(list.printList())

