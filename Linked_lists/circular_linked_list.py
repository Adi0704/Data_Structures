class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

def insert_at_beg(data,last=None):
    new=Node(data)
    if last is None:
        new.next=new
        return new
    new.next=last.next
    last.next=new
    return last

def insert_at_end(data,last=None):
    new=Node(data)
    if last is None:
        new.next=new
        return new
    new.next=last.next
    last.next=new
    return new

def insert_at_pos(data,pos,last=None):

    if last is None:
        new=Node(data)
        new.next=new
        return new

    if pos==1:
        return insert_at_beg(data,last)

    new=Node(data)

    temp=last.next

    for i in range(pos-2):
        temp=temp.next
        if temp==last.next:
            break

    new.next=temp.next
    temp.next=new

    if temp==last:
        last=new

    return last

def print_list(last):

    if last is None:
        return

    head=last.next
    temp=head

    while True:
        print(temp.data,"->",end="")
        temp=temp.next

        if temp==head:
            break


last=insert_at_beg(6)
print_list(last)
print("\n")
last=insert_at_beg(10,last)
print_list(last)
print("\n")
last=insert_at_beg(15,last)
print_list(last)
print("\n")
last=insert_at_end(23,last)
print_list(last)
print("\n")
last=insert_at_pos(20,3,last)
print_list(last)
print("\n")
last=insert_at_pos(33,1,last)
print_list(last)
print("\n")
last=insert_at_pos(89,10,last)
print_list(last)
print("\n")