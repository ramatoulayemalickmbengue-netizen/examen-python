
phrase = input("Entrez une phrase : ")
phrase_minuscule = phrase.lower()
liste_mots = phrase_minuscule.split()
print("Phrase en minuscules :", phrase_minuscule)
print("Liste des mots :", liste_mots)

nombre_mots = len(liste_mots)
mot_plus_long = max(liste_mots, key=len)
voyelles = "aeiouy"
nombre_voyelles = 0

for lettre in phrase_minuscule:
    if lettre in voyelles:
        nombre_voyelles += 1

nouvelle_phrase = []

for mot in liste_mots:
    if len(mot) % 2 == 0:
        nouvelle_phrase.append(mot.upper())
    else:
        nouvelle_phrase.append(mot)

phrase_finale = " ".join(nouvelle_phrase)

print("Nombre total de mots :", nombre_mots)
print("Mot le plus long :", mot_plus_long)
print("Nombre total de voyelles :", nombre_voyelles)
print("Nouvelle phrase :", phrase_finale)
