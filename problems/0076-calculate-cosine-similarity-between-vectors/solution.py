
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
    dot_product = 0
    sum_v1 = 0
    sum_v2 = 0
    if len(v1) == len(v2):
        for i,j in zip(v1, v2):
            dot_product+= i*j
            sum_v1+= i ** 2
            sum_v2+= j ** 2

        return round(dot_product / (sum_v1**0.5 * sum_v2**0.5), 3)
    
	
