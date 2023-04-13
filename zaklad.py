import random 
 
print("Witaj na naszej stronie ") 
print("W kuponie masz szanse wygrac 100zl psc lub sluchawk warte 200zl (oczywiscie w kuponie pro) - koszt 50zl ") 
print("A w kuponie noob - koszt 5 zl masz szanse wygrac max 30zl psc")
a=input("Jesli chcesz kupic kupon pro napisz 'pro' a jak kupon noob napisz 'noob' ") 
lista=['100zl psc', 'nic', 'sluchawki warte 200zl' , 'rabat 10% na allegro' , 'rabat na park wodny' '20zl psc'] 
lista2=['20zl psc', '30zl psc' , 'sprobuj ponownie', 'nic' 'nie tym razem' '5zl paypal' 'rabat na kebaba 10%' 'rabat na pizze 15% w pizze hut'] 
x=random.choice(lista) 
y=random.choice(lista2) 
if a=='pro': 
    print("Wygrales" , x) 
elif a=='noob': 
    print("Wygrales" , y) 
else: 
    print("error") 


 