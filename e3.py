"""
Guillem González Rodríguez
ASIXc 1C
23/1/2024


Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i
afegir la traducció en castellà, anglès i klingon. El programa, demanarà a l’usuari que escrigui per teclat un insult,
en català, i el mostrarà traduït a castellà, anglès i klingon.
"""

insults = [["IMBÈCIL", "IDIOTA", "ESTUPID", "MOCÓS", "TONTO", "PIXAPINS", "POCA-TRAÇA", "SAPASTRE", "SÒMINES",
            "FRANCÈS"],
           ["IMBECIL", "IDIOTA", "ESTÚPIDO", "MOCOSO", "TONTO", "PIJO DE CIUDAD", "POCA-TRAZA", "MORLACO",
            "FILIMINCIAS", "FRANCÉS"],
           ["IMBECILE", "IDIOT", "STUPID", "BRAT", "FOOL", "CITY SNOB", "LITTLE-TRACE", "CUNT", "FUCKWIT", "FRENCH"],
           ["TLHAQ", "QIJ", "JILOB", "DOGH", "MOL", "QIP", "GHITLH", "VAJ QIMMOH", "SAB", "BAH"]]

insult = str.upper(input())

cat = insults[0]
cast = insults[1]
ang = [2]
kli = [3]

if insult in cat or insult in cast or insult in ang or insult in kli:
    for n in range(len(insults)):
        for m in range(len(insults[n])):
            if insult == insults[n][m]:
                print("\n", cat[m], "\n", cast[m], "\n", ang[m], "\n", kli[m])

else:
    print("palabra no encontrada")
