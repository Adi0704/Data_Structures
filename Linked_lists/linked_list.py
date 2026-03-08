class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)

Node1.next=Node2
Node2.next=Node3
head=Node1

def insert_at_beginning(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
    return head

def insert_at_end(head,data):
    new_node=Node(data)
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.next=new_node

def insert_at_pos(head,pos,data):
    new_node=Node(data)
    if pos==1:
        head=insert_at_beginning(head,data)
        return head
    curr=head
    for i in range(pos-2):
        curr=curr.next
    new_node.next=curr.next
    curr.next=new_node
    return head

def delete_from_beg(head):
    temp=head
    head=head.next
    temp=None
    return head

def delete_from_end(head):
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr=None
    return head

def delete_from_pos(head,pos):
    if pos==1:
        head=delete_from_beg(head)
        return head
    curr=head
    for i in range(pos-2):
        curr=curr.next
    curr.next=curr.next.next
    return head
# 3
# 0 ->1->2
#12->13->14->15->16
def print_list(head):
    curr=head
    while curr is not None:
        print(f"{curr.data}"+"->",end="")
        curr=curr.next
    print("None")
# Example usage:
print("Original list:")
print_list(head)
head=insert_at_beginning(head,5)
print("\nAfter inserting 5 at the beginning:")
print_list(head)
insert_at_end(head,40)
print("\nAfter inserting 40 at the end:")
print_list(head)
head=insert_at_pos(head,3,3)
print("\nAfter inserting 3 at position 3:")
print_list(head)
# head=delete_from_beg(head)
# print("\nAfter deleting from Beginning:")
# print_list(head)
# head=delete_from_end(head)
# print("\nAfter deleting from Ending:")
# print_list(head)
head=delete_from_pos(head,3)
print("\n After deleting from position 3 is ")
print_list(head)


