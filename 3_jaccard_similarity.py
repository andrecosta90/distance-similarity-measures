#
#Desenvolvido por Andre H. Costa Silva
#
def intersect(a, b):
     return list(set(a) & set(b))

def union(a, b):
     return list(set(a) |set(b))

def jaccard_similarity(a,b):
    return 1.0*len(intersect(a,b))/len(union(a,b))

def calc_bag(bag,d1,d2):
    for element in bag:
        if element not in d1:
            d1[element] = 0
        if element not in d2:
            d2[element] = 0
        d1[element] += 1
    return d1,d2

def bag_jaccard_similarity(a,b):
    dA = {}
    dB = {}
    
    dA,dB = calc_bag(a,dA,dB)
    dB,dA = calc_bag(b,dB,dA)
    

    lenIntersect = 0.0
    for key in dA:
        if dA[key] > 0 and dB[key] > 0:
            lenIntersect += min(dA[key],dB[key])

    lenUnion = (len(a) + len(b)) * 1.0

    return lenIntersect / lenUnion

    

S = [1,2,3,4,5]
T = [3,4,5,6,7,8]

print jaccard_similarity(S,T)

a = [1,1,1,2]
b = [1,1,2,2,3]


print bag_jaccard_similarity(a,b)
