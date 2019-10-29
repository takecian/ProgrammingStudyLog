def removeKthNodeFromEnd(head, k):
    # Write your code here.

    first = head
    count = 1
    while count <= k:
        count += 1
        first = first.next

    if first is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    second = head
    while first.next is not None:
        first = first.next
        second = second.next
    second.next = second.next.next

