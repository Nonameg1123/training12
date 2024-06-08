class node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.head.prev=t
            t.next=self.head
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def revdisplay(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1.next and t1!=t):
            if t.data==x or t1.data==x:
                print("Found")
                return
            t=t.next
            t1=t1.prev
        if(t.data==x):
            print("Found")
            return
        print("not found")
        return
    def evenodd(self):
        t=self.head
        t1=self.tail
        while(t!=None or t1!=None):
            if t==t1:
                print("odd")
                return
            if t.next==t1:
                print("even")
                return
            t=t.next
            t1=t1.prev
    def palindrome(self):
        t=self.head
        t1=self.tail
        while(t1!=t):
            if t.data!=t1.data:
                print("not palindrome")
                return
            t=t.next
            t1=t1.prev
        print("palindrome")
        return
    def tran(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
        secondhead=slow
        secondtail=slow.prev
        secondtail.next=None
        secondhead.prev=None
        self.tail.next=self.head
        self.head.prev=self.tail
        self.head=secondhead
        self.tail=secondtail


        

a=dll()
n=int(input())
while(n!=0):
    a.addback(input())
    n-=1
a.display()
print()
s=input("search")
a.search(s)
a.evenodd()
a.palindrome()
a.tran()
a.display()