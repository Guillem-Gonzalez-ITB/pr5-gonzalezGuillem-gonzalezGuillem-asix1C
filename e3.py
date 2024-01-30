"""
Guillem González Rodríguez
ASIXc 1C
23/1/2024


Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i
afegir la traducció en castellà, anglès i klingon. El programa, demanarà a l’usuari que escrigui per teclat un insult,
en català, i el mostrarà traduït a castellà, anglès i klingon.
"""

INSULTS = (("IMBÈCIL", "IDIOTA", "ESTUPID", "MOCÓS", "TONTO", "PIXAPINS", "POCA-TRAÇA", "SAPASTRE", "SÒMINES",
            "FRANCÈS"),
           ("IMBECIL", "IDIOTA", "ESTÚPIDO", "MOCOSO", "TONTO", "PIJO DE CIUDAD", "POCA-TRAZA", "MORLACO",
            "FILIMINCIAS", "FRANCÉS"),
           ("IMBECILE", "IDIOT", "STUPID", "BRAT", "FOOL", "CITY SNOB", "LITTLE-TRACE", "CUNT", "FUCKWIT", "FRENCH"),
           ("TLHAQ", "QIJ", "JILOB", "DOGH", "MOL", "QIP", "GHITLH", "VAJ QIMMOH", "SAB", "BAH"),
           ("IMBÈCIL", "IDIOTA", "ESTUPID", "MOCÓS", "TONTO", "PIXAPINS", "POCA-TRAÇA", "SAPASTRE", "SÒMINES",
            "FRANCÈS"),
           ("IMBECIL", "IDIOTA", "ESTÚPIDO", "MOCOSO", "TONTO", "PIJO DE CIUDAD", "POCA-TRAZA", "MORLACO",
            "FILIMINCIAS", "FRANCÉS"),
           ("IMBECILE", "IDIOT", "STUPID", "BRAT", "FOOL", "CITY SNOB", "LITTLE-TRACE", "CUNT", "FUCKWIT", "FRENCH"))
EXTRALIST = 3

insult = str.upper(input())

cat = INSULTS[0]
cast = INSULTS[1]
ang = INSULTS[2]
kli = INSULTS[3]

if insult in cat or insult in cast or insult in ang or insult in kli:
    for n in range(len(INSULTS)-EXTRALIST):
        for m in range(len(INSULTS[n])):
            if insult == INSULTS[n][m]:
                print("\n", INSULTS[n+1][m], "\n", INSULTS[n+2][m], "\n", INSULTS[n+3][m])

else:
    print("palabra no encontrada")

