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
    def search(self,data):
        t=self.head
        while(t!=None):
            if t.data==data:
                return True
            t=t.next
        return False
    def mid_node(self):
        # tl=(self.l//2)
        # if self.l%2==0:
        #     t1=t1-1
        #     t1=self.head
        #     while(tl!=0):
        #         t1=t1.next
        #         tl-=1
        #     print(t1.data,t1.next.data)
        # else:
        #     t1=self.head
        #     while(tl!=0):
        #         t1=t1.next
        #         tl-=1
        #     print(t1.data)
        sl=self.head
        fs=self.head
        while(fs and fs.next):
            sl=sl.next
            fs=fs.next.next
        print(sl.data)
    def evenodd(self):
        sl=self.head
        fs=self.head
        c=0
        while(fs and fs.next):
            sl=sl.next
            c+=1
            fs=fs.next.next

        # if c%2 == 0:
        #     print("Even")
        # else:
        #     print("Odd")
        if fs:
            print("Odd")
        else:
            print("Even")
    def combo(self):
        t=self.head
        
        while t.next:
            t1=t.next
            while t1:
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
l1=sll()
num=int(input("Number"))
while(num!=0):
    l1.addback(int(input()))
    num-=1
l1.display()
print()
l1.combo()