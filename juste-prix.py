import random

def jeu_juste_prix():
    print("Bienvenue dans le jeu du Juste Prix !")
    niveau = input("Choisissez le niveau de difficulté (1 pour débutant / 2 pour intermédiaire) : ")

    if niveau == "1":
        min_nombre = 1
        max_nombre = 100
    elif niveau == "2":
        min_nombre = 1
        max_nombre = 200
    else:
        print("Choix de niveau invalide. Veuillez entrer 1 pour débutant ou 2 pour intermédiaire.")
        return

    if niveau == "1":
        nom_niveau = "débutant"
    else:
        nom_niveau = "intermédiaire"

    print(f"Niveau sélectionné : {nom_niveau}")
    print(f"Je vais choisir un nombre entre {min_nombre} et {max_nombre}, à vous de deviner lequel.")

    nombre_a_deviner = random.randint(min_nombre, max_nombre)
    nombre_devine = False
    nombre_coups = 0

    while not nombre_devine:
        coup = int(input("Entrez un nombre : "))
        nombre_coups += 1

        if coup < nombre_a_deviner:
            print("C'est plus grand !")
        elif coup > nombre_a_deviner:
            print("C'est plus petit !")
        else:
            print(f"Félicitations ! Vous avez trouvé le nombre en {nombre_coups} coups.")
            nombre_devine = True

jeu_juste_prix()
