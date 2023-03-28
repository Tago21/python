#gra zgadnij liczbe 
import random 

y=random.randint(1,100) 
print("Witaj w grze zgadnij liczbe ") 
x=int(input ("Podaj liczbe ")) 

while x!=y: 

    if x>y: 
        print("Za duzo, podaj mniej  ") 
        x=int(input("Podaj jeszcze raz "))
    elif x<y: 
        print("Za malo, podaj wiecej  ") 
        x=int(input("Podaj jeszcze raz ")) 
    elif x==y: 
        print("BRAWO, ZGADLES ") 
    else: 
        print("error")      
print("Brawo WYGRALES ") 
print("Szukana liczba to: ",y)  