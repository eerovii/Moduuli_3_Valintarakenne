import sys
import os

vuosiluku = input("Ilmoita vuosiluku, niin kerron onko se karkausvuosi: ")
os.system("cls" if os.name == "nt" else "clear")

try:
	val = int(vuosiluku)
except:
	sys.exit("Vain numerot kelpaavat!")

luku = int(vuosiluku) % 4
luku1 = int(vuosiluku) % 100

tasa2 = ""

if luku == 0:
	print("Vuosi ", vuosiluku, " on karkausvuosi.")
elif luku == 0:
	luku1 = int(vuosiluku) % 400
elif luku1 == 0:
	print("Vuosi ", vuosiluku, " on karkausvuosi.")
else:
	print("Vuosi ", vuosiluku, " ei ole karkausvuosi")