# Kuinka monta n pituista porrassanaa voidaan muodostaa kirjaimista A ... Z ?
# Porrassana: esim 'ABCBC' tai 'EFGHIJK'

def laskuri(i,pituus,maxpituus,summa,muisti):
	pituus += 1
	tempkey = str(i) + '{:02d}'.format(pituus)
	if tempkey in muisti.keys():
		return(muisti[tempkey])		
	elif pituus == maxpituus and i >= 0 and i < 26:
		return(1)
	elif i < 0 or i >= 26:
		return(0)
	else:
		temp1 = 0
		temp2 = 0
		temp1 += laskuri(i-1,pituus,maxpituus,temp1,muisti)
		newkey = str(i-1) + '{:02d}'.format(pituus+1)
		muisti[newkey] = temp1
		temp2 += laskuri(i+1,pituus,maxpituus,temp2,muisti)
		newkey = str(i+1) + '{:02d}'.format(pituus+1)
		muisti[newkey] = temp2
		summa = summa + temp1 + temp2
		return(summa)

maxpituus = 50 # Porrassanan pituus
tulos = 0
muisti = dict()
for k in range(0,26):
	tulos += laskuri(k,0,maxpituus,0,muisti)

print("Tulos: ", tulos)
