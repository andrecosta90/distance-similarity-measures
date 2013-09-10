#
#Desenvolvido por Andre H. Costa Silva
#
import math

def intersect(x,y):
     return list(set(x) & set(y))

def union(x,y):
     return list(set(x) |set(y))

def jaccard_similarity(x,y):
    return 1.0*len(intersect(x,y))/len(union(x,y))

def jaccard_distance(x,y):
    return 1.0 - jaccard_similarity(x,y)


def norm(x,y):
    if len(x) < len(y):
         size = len(y) - len(x)
         l = ['0']*size
         l.extend(list(x))
         x = ''.join(l)
    elif len(x) > len(y):
         size = len(x) - len(y)
         l = ['0']*size
         l.extend(list(y))
         y = ''.join(l)
    return x,y

#L2-norm, that is, r = 2.0
def euclidean_distance(x,y,r=2.0):
    try:
        
        return sum(((x[i] - y[i]) ** r) for i in xrange(len(x))) ** (1.0/r)
    
    except (ValueError,ZeroDivisionError):
        print 'Please, enter only even values for "r > 0".'
    except IndexError:
        print 'Please, the sets must have the same size.'

#L1-norm, that is, r = 1.0
def manhattan_distance(x,y,r=1.0):
    try:
        
        return sum([(math.fabs(x[i] - y[i]) ** r) for i in xrange(len(x))]) ** (1.0/r)
    
    except IndexError:
        print 'Please, the sets must have the same size.'

def cosine_distance(x,y):
    prodAB = sum([x[i]*y[i] for i in xrange(len(x))])
    zeros = [0 for i in xrange(len(x))]
    A = euclidean_distance(x,zeros)
    B = euclidean_distance(y,zeros)
    return prodAB / (A*B)

def edit_distance(x,y):
    dx = {}
    dy = {}

    for char in x:
         if char not in dx:
              dx[char] = 0
         if char not in dy:
              dy[char] = 0
         dx[char] += 1

    for char in y:
         if char not in dx:
              dx[char] = 0
         if char not in dy:
              dy[char] = 0
         dy[char] += 1

    LCS = []
    for key in dx:
         if dx[key] > 0 and dy[key] > 0:
              LCS.append(key)

    result = len(x)+len(y) - 2*len(LCS)
    
    return len(x) if result == 0 and x != y else result


def hamming_distance(x,y):
    x,y = norm(x,y)
    return len([i for i in xrange(len(x)) if x[i] != y[i]])
          
    
    
x = [2,7]
y = [6,4]


#print jaccard_similarity(x,y)
#print cosine_distance(x,y)

#print jaccard_distance(S,T)

#print euclidean_distance([2,7],[6,4])
#print euclidean_distance([2,7],[6,4],100)
#print manhattan_distance([2,7],[6,4])
#print manhattan_distance([2,7],[6,4],2)
#print manhattan_distance([2,7],[6,4],100)


#a = 'antonionunes'
#b = 'testetestando'
#print edit_distance('abcde','acfdeg')
#print edit_distance('aba','bab')
#print edit_distance('ab','ba')

#print edit_distance(a,b)
#print edit_distance('kitten','sitting')
#print edit_distance('aba','bab')
#print edit_distance('antonio','andre')
#print edit_distance('andre','antonio')

x = '10101'
y = '11110'
#print hamming_distance(x,y)


print hamming_distance('011101','10')
print hamming_distance('10','011101')
