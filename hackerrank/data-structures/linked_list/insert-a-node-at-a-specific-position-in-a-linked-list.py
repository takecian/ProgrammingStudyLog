#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    n = SinglyLinkedListNode(data)
    count = 0
    cursor = dummy
    while cursor:
        if count == position:
            temp = cursor.next
            cursor.next = n
            n.next = temp
            break
        else:
            cursor = cursor.next
            count += 1
    return dummy.next
