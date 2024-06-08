class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self) -> None:
        self.head=None
        self.l=0
    def addback(self,data):
        self.l+=1
        if self.head==None:
            self.head=node(data)
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            t.next=node(data)
    def addfront(self,data):
        self.l+=1
        t=node(data)
        t.next=self.head
        self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def bub(self):
        f=0
        t=self.head
        c=self.head
        b=None
        while c.next:
            while (t.next!=b):
                if t.data>t.next.data:
                    t.data,t.next.data=t.next.data,t.data
                    f=1
                t=t.next
            if f==0:
                break
            b=t
            t=self.head
            c=c.next
   
   
l1=sll()
num=int(input("Number"))
while(num!=0):
    l1.addback(int(input()))
    num-=1
l1.display()
print()
l1.bub()
l1.display()
