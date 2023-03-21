a=0
b=0
import random 
print("Witaj zagrajmy w papier, kamien, nozyce ")  
x=input("Podaj cios ") 
lista=["kamien","nozyce", "papier"] 
y=random.choice(lista)  
print (y) 
while a==3 or b==3: 
    print("Koniec") 
if x==  "kamien" and y=="nozyce": 
    print("Wygrales") 
    a=a+1 
elif x=="nozyce" and y=="papier": 
    print("Wygrales")
    a=a+1 
elif x=="papier" and y=="kamien": 
    print("Wygrales") 
    a=a+1 
elif x=="kamien" and y=="papier": 
    print("Przegrales") 
    b=b+1
elif x=="nozyce" and y=="kamien": 
    print("Przegrales") 
    b=b+1
elif x=="papier" and y=="nozyce": 
    print("Przegrales") 
    b=b+1 
elif x=="papier" and y=="papier":
    print("Remis ") 
elif x=="kamien" and y=="kamien": 
    print("Remis") 
elif x=="nozyce" and y=="nozyce": 
    print("Remis") 
else: 
    print("error") 

print ("wynik koncowy to:")
print (a) 
print(b) 