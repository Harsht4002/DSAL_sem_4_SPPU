# To create ADT that implement the "set" concept. a. Add (new Element) -Place a value into the set , b. Remove (element) Remove the value 
# c. Contains (element) Return true if element is in collection, d. Size () Return number of values in collection Iterator () Return an 
# iterator used to loop over collection, e. Intersection of two sets , f. Union of two sets, g. Difference between two sets, h. Subset
class Set:
    def __init__(self):
        self.data=[]
    def add(self,no):
        if no not in self.data:
            self.data.append(no)
    def remove(self,no):
        if no in self.data:
            self.data.remove(no)
    def contain(self,no):
        if no in self.data:
            return True
        return False
    def size(self):
        return len(self.data)
    def intersection(self,set2):
        res=set()
        for i in self.data:
            if i in set2.data:
                res.add(i)
        return res
    def union(self,set2):
        res=set()
        for i in self.data:
            res.add(i)
        for i in set2.data:
            res.add(i)
        return res
    def difference(self,set2):
        res=set()
        for i in self.data:
            if not set2.contain(i):
                res.add(i)
        for i in set2.data:
            if not self.contain(i):
                res.add(i)
        return res        
    def subset(self,set2):
        res=set()
        for i in set2.data:
            if not self.contain(i):
                return False
        return True
    def __iter__(self):
        return iter(self.data)
a=Set()
b=Set()
a.add(1)
a.add(3)
a.add(4)
a.add(5)
b.add(4)
b.add(3)
print(a.intersection(b))
print(a.difference(b))
print(a.subset(b))

