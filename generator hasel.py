import random 
import string 
#generator hasel 
print("Witaj w naszym generatorze hasel ") 

alfabet=list(string.ascii_lowercase) 
cyfry=list(range(1,101)) 
haslo=[]
for i in range(4): 
    y=random.choices(alfabet)  
    a=random.choices(cyfry)
    haslo.append(y) 
    haslo.append(a)
     
    
print(haslo) 