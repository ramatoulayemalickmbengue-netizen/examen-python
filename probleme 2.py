
students = [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Ibrahima", 7)
]

def afficher_etudiants(liste):
    print("Liste des étudiants et leurs notes :")
    for nom, note in liste:
        print(nom, ":", note)

def calculer_moyenne(liste):
    somme = 0
    for _, note in liste:
        somme += note
    return somme / len(liste)

def note_max_min(liste):
    note_max = liste[0][1]
    note_min = liste[0][1]

    for _, note in liste:
        if note > note_max:
            note_max = note
        if note < note_min:
            note_min = note

    return note_max, note_min

def classer_etudiants(liste):
    admis = []
    ajournes = []

    for nom, note in liste:
        if note >= 10:
            admis.append(nom)
        else:
            ajournes.append(nom)

    return admis, ajournes

afficher_etudiants(students)
moyenne = calculer_moyenne(students)
note_max, note_min = note_max_min(students)
admis, ajournes = classer_etudiants(students)

print("\nMoyenne de la classe :", moyenne)
print("Note maximale :", note_max)
print("Note minimale :", note_min)
print("Étudiants admis :", admis)
print("Étudiants ajournés :", ajournes)
