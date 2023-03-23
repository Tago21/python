a=0
b=0
import random 
while a<33 or b<33: 
    print("Wynik to: ") 
    print(a) 
    print(b) 
    print("Witaj zagrajmy w papier, kamien, nozyce ")  
    x=input("Podaj cios ") 
    lista=["kamien","nozyce", "papier"] 
    y=random.choice(lista)  
    print (y) 

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

