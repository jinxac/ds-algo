def getNthfromEnd(head,n):
    #code here
    p1 = head
    p2 = head

    while n > 1 and p2 is not None:
        n -= 1
        p2 = p2.next

    if p2 is None:
        return -1

    while p2.next != None:
        p1 = p1.next
        p2 = p2.next

    return p1.data