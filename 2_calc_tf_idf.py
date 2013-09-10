#
#Desenvolvido por Andre H. Costa Silva
#
'''
TF.IDF (Term Frequency times In- verse Document Frequency)

The formal measure of how concentrated into relatively few documents are
the occurrences of a given word.
'''

import math

def get_frequency(D):
    frequency = {} #number of occurrences
    max_frequency = {}
    for doc in D:
       max_frequency[doc] = -float('inf')
    
    for doc in D:
        d = doc.split(' ')
        for word in d:
            key = (word,doc)
            if key not in frequency:
                frequency[key] = 0.0
            frequency[key] += 1.0

            if max_frequency[doc] < frequency[key]:               
               max_frequency[doc] = frequency[key]
            
    return frequency,max_frequency

      

def calc_term_frequency(D):
   frequency,max_frequency = get_frequency(D)
   tf = {}
   for doc in D:
      d = doc.split(' ')
      for word in d:
         key = (word,doc)
         tf[key] = frequency[key]/max_frequency[doc]
         
   return tf

def calc_inverse_document_frequenc(D):

   #ni => em quantos docs. a palavra 'word' aparece
   ni = {}
   for doc in D:
      d = doc.split(' ')
      for word in d:
         if word not in ni:
            ni[word] = 0.0
            
   for word in ni:
      for doc in D:
         if word in doc:
            ni[word] += 1.0

   N = len(D) * 1.0
   idf = {}
   for word in ni:
      idf[word] = math.log((N/ni[word]),2)
   return idf

def calc_tf_idf(D):
   tf = calc_term_frequency(D)
   idf = calc_inverse_document_frequenc(D)

   w = {}
   for doc in D:
      d = doc.split(' ')
      for word in d:
         key = (word,doc)
         w[key] = tf[key] * idf[word]
   return w
    
d1 = "A A A B"
d2 = "A A C"
d3 = "A A"
d4 = "B B"

D = [d1,d2,d3,d4]
w = calc_tf_idf(D)

print w
