class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def insert_at_beg(data,head=None):
    curr=Node(data)
    if head is None:
        return curr
    curr.next=head
    head.prev=curr
    return curr

def insert_at_end(data,head):
    temp=Node(data)
    if head is None:
        return insert_at_beg(data)
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.next=temp
    temp.prev=curr
    return head

def insert_at_pos(data,head,pos):
    temp=Node(data)
    if pos==1:
        temp.next=head
        head.prev=temp
        head=temp
        return head
    if head is None:
        insert_at_beg(data)
    curr=head
    for i in range(pos-2):
        if curr is None:
            break
        curr=curr.next 
    if curr is None:
        return head
    temp.next = curr.next
    temp.prev = curr

    if curr.next:
        curr.next.prev = temp

    curr.next = temp
    print_list(head)
    return head    
def print_list(head):
    curr=head
    while curr is not None:
        print(f"{curr.data}"+"<->",end="")
        curr=curr.next
    print("None")
    
head=insert_at_beg(2)
print("\n After inserting at beginning :")
print_list(head)
head=insert_at_beg(3,head)
head=insert_at_beg(4,head)
print_list(head)
head=insert_at_end(19,head)
print_list(head)
head=insert_at_pos(21,head,2)