class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class cse:
    def __init__(self):
        self.head = None

    def creat(self, x):
        if self.head is None:
            self.head = node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def dispaly(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
        

b = cse()
b.creat(20)
b.creat(30)
b.add_front(60)
b.creat(40)
b.display()
print(b.head.next.data)