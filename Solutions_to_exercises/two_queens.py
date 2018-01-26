# N Queens problem, mutta kahdella kuningattarella ja vapaavalintaisen kokoisella (suurella) laudalla.
# Tavoitteena ratkaista, että monellako tapaa nappulat voidaan sijoittaa siten, että ne eivät uhkaa toisiaan.
#
# In English: N Queens problem, but with two queens and board of own choosing (variable n).

import time
import numpy as np
from math import factorial as fa
import operator as op
import functools

def nCr(n, r):
	r = min(r, n-r)
	if r == 0:
		return 1
	else:
		numer = functools.reduce(op.mul, range(n, n-r, -1))
		denom = functools.reduce(op.mul, range(1, r+1))
		return(numer//denom)

alku = time.time()
print("Aloitus")
n = 12345 # Laudan sivun pituus. Lauta = n*n
npow = n**2

summa = 0
valisumma = 0

#print("Checkpoint 1")

valisumma = 4 * ((fa(n)) / (fa(n-3)*fa(3)))
#print("Checkpoint 2")
summa += (2*n + 2) * ((fa(n)) / (fa(n-2)*fa(2)))
#print("Checkpoint 3")
summa += valisumma
#print("Checkpoint 4")
kaikki = nCr(npow,2)
#print("Checkpoint 5")
print("")
print("Mahdollisia sijoituksia:")
print("Hyokkayksia: ", int(summa))
print("Kaikki tavat: ", int(kaikki))

tulos = kaikki - summa

print("Aika: ",time.time() - alku)
print("")
print("Tulos: ", int(tulos))
