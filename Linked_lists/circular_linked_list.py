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

def print_list(last):
    if last is None:
        return
    
    head=last.next
    temp=head
    while True:
        print(f"{temp.data}"+" ->",end="")
        temp=temp.next
        if temp!=head:
            continue
        else:
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