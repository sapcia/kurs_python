l = ['i', 'c', 0, 'm']
l[0] = "I"
del l[2]
print(l)

for i in range(len(l)):
	print(l[i])
	l[i] = "q"
print(l)

s = 'asdfghjkl'
l = list(s)
l[2] = "X"
del(l[5])
s = "".join(l)
print(s)

l =['i', 'm']
l.insert(1, 'c')
print(l)
l.reverse()
print(l)
l.sort()
print(l)
#Zadanie 4.3.1
def parse(zdanie):
		t= zdanie.replace("XY", " ")
		return t.split(":")
print(parse("Ala:maXYkotka:i inne:zwierzeta"))	
#Zadanie 4.3.2
def sortowanie(x):
	x.sort()
	x.reverse()
	return x
print(sortowanie(['Agata', 'Lukasz', 'Mariusz', 'Szczepan', 'Igor', 'Michal', 'Konstanty']))

#Zadanie 4.3.3
def sortuj(lista):
	l = lista.copy()
	l.sort()
	return l
print(sortuj(['Monika', 'Zbyszek', 'Barbara', 'Agata', 'Lukasz', 'Mariusz', 'Szczepan', 'Igor', 'Michal', 'Konstanty']))	


# SLOWNIKI

slownik = {"bd" : "xx", 5 : True, "a" : 11}
for klucz in slownik:
	print(klucz, "=>", slownik[klucz])
	
if "bd" in slownik:
	print("jest elementem slownika o kluczu 'bd'")
	del slownik['bd']

slownik["15"] = True
slownik["a"] = "yy"	

print(klucz, "=>", slownik[klucz])


dict = {'Name': 'Zabra', 'Age': 7}
print("Value", "Age",": ",  dict.get('Age'))
print("Value : ",  dict.get('Education', "Never"))

## zadanie 4.4.1
def zlicz(lista):
	s={}
	for w in lista:
		s[w] = s.get(w,0)+1
	for k in s:	
		print(str(k) + " wystepuje " + str(s[k]) + " razy")
zlicz(["AX", "B", "AX", "AX", 'AX'])
def zlicz(x):
	s = {}
	for e in x:
		s[e] = s.get(e, 0) +1
	for k in s:
		print(str(k) + " wystepuje " + str(s[k]) + " razy")
zlicz(["AX", "B", "AX"])
# zadanie 4.4.2
#def konwersja(lista):
#	s = {}
#	for w in lista:
#		poz = w.find("=")
#		s[w[0:poz]]
		
		
#Zadanie 4.4.2
def konwert(x):
	s={}
	for w in x:
		poz = w.find("=")
		s[w[0:poz]] = w[poz+1:]
	return s
print(konwert(["aa=13", "b=Ala=kot", "f=xyz"]))

mapa = {'5' : 3, 'bd' : 20, 'a' : 101}
lista = sorted(mapa.items())
print(lista)		

#Funckja jako argument funckji

def dzialanie(operacja):
	if operacja == "dodaj":
		def f(a, b):
			return a+b
		return f
	elif operacja == "mnoz":
		def f(a, b):
			return a*b
		return f
def dwa(funkcja, argument):
	return funkcja(2, argument)
d = dzialanie("dodaj")
a = dwa(d, 11)
b = dzialanie("mnoz")(4,4)
print(a, b)

#Zadanie 4.5.1
def dzialanie_s(x):
	s = { "dodaj" : (lambda a, b: a + b), "mnoz" : (lambda a, b: a * b)}
	return s.get(x)
a=dzialanie_s("mnoz")(4,5)
print(a)

#Zadanie 4.5.2
print("Zadanie 4.5.2")
def wykonaj(lista, funckja):
	for x in lista:
		funckja(x)

print(wykonaj([1, 2, 3], print))
print(wykonaj(["Ala", 2, 3], print))
print(wykonaj["aa=13", "b=Ala=kot", "f=xyz"],konwert)
