# Ohjelma, joka muuntaa kirjaimet sanoiksi.
# Esim: 999 = "yhdeksänsataayhdeksänkymmentäyhdeksän"
# Toimii luvuilla 1 ... 999 999 999

lukutiedosto = open("luvut.txt", "r")
luvut = lukutiedosto.readlines()
lukutiedosto.close()

kirjoitustiedosto = open("luvut_vastaus.txt", "w")

sanat = ['nolla','yksi','kaksi','kolme','neljä','viisi','kuusi','seitsemän','kahdeksan','yhdeksän']
sanat_toista = ['toista']
sanat_kymmenta = ['kymmenen','kymmentä']
sanat_sataa = ['sata','sataa']
sanat_tuhatta = ['tuhat','tuhatta']
sanat_miljoonaa = ['miljoona','miljoonaa']

count = 1

for luku in luvut:
	luku = '{:09d}'.format(int(luku))
	
	tuloste = ''
	
# ---------------------------------------------------------------------
	if int(luku[0]) != 0: # sadat miljoonat
		if int(luku[0]) != 1: # X sataa
			tuloste = tuloste + sanat[int(luku[0])] + sanat_sataa[1]
		else: # sata
			tuloste = tuloste + sanat_sataa[0]
	if int(luku[1]) != 0: # kymmenet miljoonat
		if int(luku[1]) != 1: # X kymmentä
			tuloste = tuloste + sanat[int(luku[1])] + sanat_kymmenta[1]
		elif int(luku[1]) == 1 and int(luku[2]) == 0: # kymmenen
			tuloste = tuloste + sanat_kymmenta[0]
	if int(luku[2]) != 0: # miljoonat
		if int(luku[1]) == 1: # X-toista
			tuloste = tuloste + sanat[int(luku[2])] + sanat_toista[0]
		elif int(luku[2]) == 1 and int(luku[1]) == 0 and int(luku[0]) == 0:
			a = 1 # empty
		else: # X
			tuloste = tuloste + sanat[int(luku[2])]
# -----------------------------------------------------------------
	if int(luku[0]) != 0 or int(luku[1]) != 0 or int(luku[2]) != 0: # -miljoonaa
		if int(luku[0]) == 0 and int(luku[1]) == 0 and int(luku[2]) == 1:
			tuloste = tuloste + sanat_miljoonaa[0]
		else:
			tuloste = tuloste + sanat_miljoonaa[1]
# ---------------------------------------------------------------------
	if int(luku[3]) != 0:
		if int(luku[3]) != 1: # X sataa
			tuloste = tuloste + sanat[int(luku[3])] + sanat_sataa[1]
		else: # sata
			tuloste = tuloste + sanat_sataa[0]
	if int(luku[4]) != 0:
		if int(luku[4]) != 1: # X kymmentä
			tuloste = tuloste + sanat[int(luku[4])] + sanat_kymmenta[1]
		elif int(luku[4]) == 1 and int(luku[5]) == 0: # kymmenen
			tuloste = tuloste + sanat_kymmenta[0]
	if int(luku[5]) != 0:
		if int(luku[4]) == 1: # X-toista
			tuloste = tuloste + sanat[int(luku[5])] + sanat_toista[0]
		elif int(luku[5]) == 1 and int(luku[4]) == 0 and int(luku[3]) == 0:
			a = 1 # empty
		else: # X
			tuloste = tuloste + sanat[int(luku[5])]
# -----------------------------------------------------------------
	if int(luku[3]) != 0 or int(luku[4]) != 0 or int(luku[5]) != 0: # -tuhatta
		if int(luku[3]) == 0 and int(luku[4]) == 0 and int(luku[5]) == 1:
			tuloste = tuloste + sanat_tuhatta[0]
		else:
			tuloste = tuloste + sanat_tuhatta[1]
# ---------------------------------------------------------------------
	if int(luku[6]) != 0: # sadat
		if int(luku[6]) == 1: # sata
			tuloste = tuloste + sanat_sataa[0]
		else: # X sataa
			tuloste = tuloste + sanat[int(luku[6])] + sanat_sataa[1]
	if int(luku[7]) != 0: # kymmenet
		if int(luku[7]) != 1: # X kymmentä
			tuloste = tuloste + sanat[int(luku[7])] + sanat_kymmenta[1]
		elif int(luku[7]) == 1 and int(luku[8]) == 0: # kymmenen
			tuloste = tuloste + sanat_kymmenta[0]
	if int(luku[8]) != 0: # yhdet
		if int(luku[7]) == 1: # X-toista
			tuloste = tuloste + sanat[int(luku[8])] + sanat_toista[0]
		else: # X
			tuloste = tuloste + sanat[int(luku[8])]
	
	print(count)
	print(luku)
	kirjoitustiedosto.write(tuloste)
	kirjoitustiedosto.write('\n')
	
	count += 1

kirjoitustiedosto.close()
