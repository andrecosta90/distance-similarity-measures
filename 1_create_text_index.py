#
#Desenvolvido por Andre H. Costa Silva
#

class Document:
    _id = ""
    _words = []
    def __init__(self,id,words):
        self._id = id
        self._words = words.split(' ')

class Index:
    __keys__ = []
    __values__ = []    
    
    def create(self,D):
        for d in D: # O (n * w * m) with list;
            for w in d._words: # O(w) => O(w * m)
                #O(m) + O(w)
                i = self.lookup(w) # O(m) => with list; O(log m) [binary trees] or O(1) if to use a good hash table
                if i < 0:
                    j = index.add(w) # O(1)
                    index.append(j,d._id) # O(w)
                else:
                    index.append(i,d._id) # O(w)
        #print self.__keys__
        #print self.__values__
                    
    def lookup(self,w):
        try:
            return self.__keys__.index(w)
        except ValueError:
            return -1
        #return __store__.find("w")

    def add(self,w):
        self.__keys__.append(w)
        self.__values__.append([])
        return len(self.__keys__) - 1

    def append(self,i,id):
        if id not in self.__values__[i]:
            self.__values__[i].append(id)


    def query(self,q):
        i = self.lookup(q)
        if i < 0:
            return []
        return self.__values__[i]



D = []

a = Document('a.com','the quick brown fox jumps over the lazy dog')
b = Document('b.com','a bird in hand is worth two in a bush')
c = Document('c.com','the lazy bird misses the worm')

D.append(a)
D.append(b)
D.append(c)

index = Index()
index.create(D)

print index.query('lazy')
