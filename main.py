import math
import time

while True:
	try:
		print("Co chccesz obliczyć?")
		print("1 - Delta")
		print("2 - p")
		print("3 - q")
		print("4 - miejsca zerowe")
		print("9 - informacje")
		print("0 - wyjdź")
		wybor = int(input("#> "))
		break
	except ValueError:
		print("To nie jest numer!")

def delta(a, b, c):
	delta = b**2-4*a*c
	return delta

def p1(x1, x2):
	p1 = (x1+x2)/2
	return p1

def p2(a, b):
	p2 = -b/(2*a)
	return p2

def q(a, b, c):
	wartosc_delta = delta(a, b, c)
	q = -(wartosc_delta) / (4*a)
	return q

def wyswietl_ramke(tekst):
    lines = tekst.split('\n')
    max_length = max(len(line) for line in lines)
    border = '#' * (max_length + 4)
    
    # Wyświetl górną ramkę
    print(border)
    
    # Wyświetl zawartość
    for line in lines:
        print(f'# {line.ljust(max_length)} #')
    
    # Wyświetl dolną ramkę
    print(border)
    
if wybor == 9:
    tekst = """Jakub Bednarczyk"""
    print(wyswietl_ramke(tekst))


if wybor == 0:
    exit

if wybor == 1:
	a = float(input("wprowadź a\n#> "))
	b = float(input("wprowadź b\n#> "))
	c = float(input("wprowadź c\n#> "))
	print(delta(a, b, c))

if wybor == 2:
	wybor1 = input("masz miejsca zerowe? y/n: ")
	if wybor1 == "y":
		x1 = float(input("wprowadź x1\n#> "))
		x2 = float(input("wprowadź x2\n#> "))
		print(p1(x1, x2))
	if wybor1 == "n":
		a = float(input("wprowadź a\n#> "))
		b = float(input("wprowadź b\n#> "))
		print(p2(a, b))

if wybor == 3:
	while True:
		try:
			a = float(input("wprowadź a\n#> "))
			b = float(input("wprowadź b\n#> "))
			c = float(input("wprowadź c\n#> "))
			print(q(a, b, c))
			break
		except ZeroDivisionError:
			print("a nie może być równe zero!")
		except ValueError:
			print("tylko liczby!")

if wybor == 4:
	while True:
		try:
			a = float(input("wprowadź a\n#> "))
			b = float(input("wprowadź b\n#> "))
			c = float(input("wprowadź c\n#> "))

			wartosc_delta = delta(a, b, c)
			if wartosc_delta < 0:
				print("Nie ma miejsc zerowych")
			if wartosc_delta == 0:
				x0 = -(b) / (2*a)
				print("Jest jedno miejsce zerowe i wynosi ono: ", x0)
			if wartosc_delta > 0:
				x1 = (-b - math.sqrt(wartosc_delta)) / (2*a)
				x2 = (-b + math.sqrt(wartosc_delta)) / (2*a)
				print("Są dwa miejsca zerowe i wynoszą: x1=", x1, " x2=", x2)
			break
		except ZeroDivisionError:
			print("0!=")


			#dodałem komentarz?