print("1.Ile wart jest 1 korona czeska na zlotowki ") 
b=0
a=input("A)0.16 B)0.18 C)0.20 ")  

if a=='A' or a=='a': 
    print("Bledna  odpowiedz ")  

elif a=='B' or a=='b': 
    print("Bledna odpowiedz ") 
elif a=='C' or a=='c': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt ") 
    b=b+1 
else: 
    print("error")
print("2.W ktorym roku byla konstytucja 3 maja ") 
c=input("A)1791 B)1688 C)1821  ") 
if c=='A' or c=='a': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt  ") 
    b=b+1 
elif c=='B' or c=='b': 
    print("Bledna odpowiedz ") 
elif c=='C' or c=='c': 
    print("Bledna odpowiedz") 
else: 
    print("error") 

print("3.Jaki kraj wygral mistrzostwa swiata w pilce noznej w 2006 roku") 
d=input("A)Hiszpania B)Niemcy C)Wlochy ") 
if d=='A' or d=='a': 
    print("Bledna odpowiedz ") 
elif d=='B' or d=='b': 
    print("Bledna odpowiedz ") 
elif d=='C' or d=='c': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt") 
    b=b+1 
else: 
    print("error")

print("4.Ile dni ma zwykly rok") 
e=input("A)366 B)365 C)355 ") 
if e=='A' or e=='a': 
    print("Bledna odpowiedz ") 
elif e=='B' or e=='b': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt ") 
    b=b+1 
elif e=='C' or e=='c': 
    print("Bledna odpowiedz ") 
else: 
    print("error") 

print("5.Co znaczy po angielsku 'deer'?  ") 
f=input("A)owca B)jelen C)losos ") 

if f=='A' or f=='a': 
    print("Bledna odpowiedz ") 
elif f=='B' or f=='b': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt ") 
    b=b+1 
elif f=='C' or f=='c': 
    print("Bledna odpowiedz ") 
else: 
    print("error") 

print("6.Stolica Chorwacji jest: ") 
g=input("A)Zagrzeb B)Sarajewo C)Belgrad  ") 
if g=='A' or g=='a': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt") 
    b=b+1 
elif g=='B' or g=='b': 
    print("Bledna odpowiedz ") 
elif g=='C' or g=='c': 
    print("Bledna odpowiedz ") 
else: 
    print("error") 

print("7.Miasto Norymberga znajduje sie w: ")  
h=input("A)Wlochy B)Niemcy C)Francja ") 
if h=='A' or h=='a': 
    print("Bledna odpowiedz ") 
elif h=='B' or h=='b': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt ") 
    b=b+1 
elif h=='C' or h=='c': 
    print("Bledna odpowiedz ") 
else: 
    print("error") 

print("8.Co jest wiecej warte przeliczajac na zlotowki  ") 
i=input("A)Rubel rosyjski B)oba maja ta sama wartosc C)Robux ") 
if i=='A' or i=='a': 
    print("Bledna odpowiedz ") 
elif i=='B' or i=='b':
    print("Bledna odpowiedz ") 
elif i=='C' or i=='c': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt ") 
    b=b+1 
else: 
    print("error") 

print("9.Jaki jest wzor na delte ?") 
m=input("A)b^2-4ac  B) c2-2ac  C) b^2-4bc") 
if m=='A' or m=='a': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt ") 
    b=b+1 
elif m=='B' or m=='b': 
    print("Bledna odpowiedz ") 
elif m=='C' or m=='c': 
    print("Bledna odpowiedz ")  
else: 
    print("error") 

print("10. Z ktorego kraju pochodzi Halland? ") 
k=input("A)Hiszpania B)Norwegia C)Anglia ") 
if k=='A' or k=='a': 
    print("Bledna Odpowiedz ") 
elif k=='B' or k=='b': 
    print("Prawidlowa odpowiedz! Zgarniasz 1 punkt ") 
    b=b+1 
elif k=='C' or k=='c': 
    print("Bledna odpowiedz ") 
else: 
    print("error") 
print("Liczba uzyskanych punkto to: ", b ) 
z=b/10 * 100 
print("Twoj wynik procentowy to: ",z, "%" ) 