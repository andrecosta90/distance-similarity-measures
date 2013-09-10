#
#Desenvolvido por Andre H. Costa Silva baseado no codigo fonte 
#de Rodrigo Mendes (implementado em javascript): https://github.com/rdgms/hello_cosine_similarity
#

import math
import string

def calculate_frequence(word):
    result = {}
    for char in string.ascii_lowercase:
        if char not in result:
            result[char] = 0.0
        for w in word:
            if char == w:
                result[char] += 1.0
    return result

def calculate_product(x,y):
    return sum([x[i]*y[i] for i in x])

def calculate_magnitude(x):
    return sum(((x[i]) ** 2.0) for i in x) ** (0.5)

word_1 = "teste"
word_2 = "testi"
word_3 = "test"

word_1_frequence = calculate_frequence(word_1)
word_2_frequence = calculate_frequence(word_2)
word_3_frequence = calculate_frequence(word_3)

words_product1 = calculate_product(word_1_frequence, word_2_frequence)
words_product2 = calculate_product(word_1_frequence, word_3_frequence)
words_product3 = calculate_product(word_2_frequence, word_3_frequence)

word_1_magnitude = calculate_magnitude(word_1_frequence)
word_2_magnitude = calculate_magnitude(word_2_frequence)
word_3_magnitude = calculate_magnitude(word_3_frequence)

#print word_1_magnitude
#print word_2_magnitude

magnitude_product1 = word_1_magnitude * word_2_magnitude
magnitude_product2 = word_1_magnitude * word_3_magnitude
magnitude_product3 = word_2_magnitude * word_3_magnitude

result1 = words_product1 / magnitude_product1
result2 = words_product2 / magnitude_product2
result3 = words_product3 / magnitude_product3

print word_1, " is " , result1,"% similar to " , word_2
print word_1, " is " , result2,"% similar to " , word_3
print word_2, " is " , result3,"% similar to " , word_3

