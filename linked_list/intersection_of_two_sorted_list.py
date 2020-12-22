def findIntersection(head1,head2):
    #return head
    curr1 = head1
    curr2 = head2
    new_node = Node(-1)
    temp_new_node = new_node

    while curr1 and curr2:
        if curr1.data > curr2.data:
            curr2 = curr2.next
        elif curr1.data < curr2.data:
            curr1 = curr1.next
        else:
            temp_new_node.next = Node(curr1.data)
            temp_new_node = temp_new_node.next
            curr1 = curr1.next
            curr2 = curr2.next

    return new_node.next