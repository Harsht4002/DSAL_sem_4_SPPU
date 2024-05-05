class node:
    def __init__(self,name,no):
        self.name=name
        self.no=no
        self.used=False
class hashtable:
    def __init__(self):
        self.data=[]
        for i in range (10):
            self.data.append(node(None,None))
    def hashfunc(self,name):
        s=0
        for c in name:
            s += ord(c)
        return s % 10
    def quadprobing(self,name):
        i=1
        while(self.data[key].used!=False):
            key=(key+(i*i))%10
            i+=1
        print("combinations required: ",i)
        return key
    def linprobing(self,key):
        i=1
        while(self.data[key].used!=False):
            key=(key+1)%10
            i+=1
        print("combinations required: ",i)
        return key
    def lininsert(self,name,no):
        key=self.hashfunc(name)
        key=self.linprobing(key)
        self.data[key]=node(name,no)
        self.data[key].used=True
    def quadinsert(self,name,no):
        key=self.hashfunc(name)
        key=self.linprobing(key)
        self.data[key]=node(name,no)
        self.data[key].used=True
    def search(self,name):
        key=self.hashfunc(name)
        index=key
        while self.data[index].used:
            if self.data[index].name==name:
                print("found. no is: ",self.data[index].no)
                return
            index+=1
            if index==key:
                break
        print("not found")
            
h=hashtable()
h.lininsert("roman",98)
h.lininsert("norma",85)
h.quadinsert("sara",23)
h.search("norma")
