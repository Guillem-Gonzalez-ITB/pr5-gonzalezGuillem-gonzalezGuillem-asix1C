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

if insult in insults[0] or insult in insults[1] or insult in insults[2] or insult in insults[3]:
    for n in range(len(insults)):
        for m in range(len(insults[n])):
            if insult == str(insults[n][m]):
                print("\n", insults[0][m], "\n", insults[1][m], "\n", insults[2][m], "\n", insults[3][m])

else:
    print("palabra no encontrada")
