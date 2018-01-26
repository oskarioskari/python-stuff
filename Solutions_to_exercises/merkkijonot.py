# Kuinka monta erilaista merkkijonoa voidaan sanasta muodostaa,
# poistamalla N > 0 kirjainta sekä pitämällä kirjainten järjestyksen samana.

import time

def vahentaja(cursor,sana,sanasetti):
	if cursor == len(sana):
		sanasetti.add(sana)
		return(sanasetti)
	else:
		uusi = sana[:cursor] + sana[cursor+1:]
		sanasetti.add(uusi)
		vahentaja(cursor+1,sana,sanasetti)
		vahentaja(cursor,uusi,sanasetti)
		return(sanasetti)

alku = time.time()

#merkkijono = "LAAJA"
#merkkijono = "HATTIVATTI"
merkkijono = "SAIPPUAKAUPPIAS"

cursor = 0
sanasetti = set()
sanasetti = vahentaja(cursor,merkkijono,sanasetti)

sanasetti.remove(merkkijono)
sanasetti.remove('')

print("\n")
print("Tarkistus:",len(sanasetti),"\n")
print("Aika: ",time.time()-alku)
