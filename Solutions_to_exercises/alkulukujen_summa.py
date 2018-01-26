# Ohjelma laskee, että kuinka monena eri alkulukujen summana valittu luku voidaan esittää.

def summia(luku,lista):
	if sum(lista) > luku:
		return(0)
	elif sum(lista) == luku:
		return(1)
	else:
		tulos = 0
		for j in range(luku,1,-1):
			uusi = []
			for item in lista:
				uusi.append(item)
			jaollinen = False
			for k in range(j-1,1,-1):
				if j%k == 0:
					jaollinen = True
			if jaollinen == False:
				uusi.append(j)
				tulos += summia(luku,uusi)
		return(tulos)

tyhja = []
luku = 25 # Tutkittava luku

print(summia(luku,tyhja))
