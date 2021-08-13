import pendu

def is_win(lettres_trouvées, mot_à_trouver):

    mot_trouvé = ""
    for lettre in mot_à_trouver:
        if lettre in lettres_trouvées:
            mot_trouvé += lettre

    if mot_trouvé == mot_à_trouver:
        return True
    return False


nombres_d_erreurs = 0
mot_à_trouver = "canard"
mot_avec_trou = ""
lettres_trouvées = [mot_à_trouver[0]]
deja_perdu = False

pas_fini = True

while pas_fini:

    # Affichage du début
    mot_avec_trou = ""
    for lettre in mot_à_trouver:
        if lettre in lettres_trouvées:
            mot_avec_trou += " " + lettre
        else:
            mot_avec_trou += " _"

    # On enlève l'espace du début
    mot_avec_trou = mot_avec_trou[1:]

    # Génération du pendu
    pendu.drawing = pendu.generate(nombres_d_erreurs, mot_avec_trou)

    if len(pendu.drawing) == 0:

        if deja_perdu == False:
            print('Vous avez perdu ! Le mot était ' + mot_à_trouver)
        deja_perdu = True

        response = input('Recommencer (O)ui/(N)on ? ').upper()
        if response == 'O':
            nombres_d_erreurs = 0
            mot_à_trouver = "canard"
            mot_avec_trou = ""
            lettres_trouvées = [mot_à_trouver[0]]
            deja_perdu = False
        elif response == 'N':
            pas_fini = False
    else:
        print("\n" + pendu.drawing)

        lettre_input = input("Entrer une lettre : ").lower()
        print("\n")

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if lettre_input in alphabet and len(lettre_input) == 1 and lettre_input not in lettres_trouvées:
            if lettre_input in mot_à_trouver:
                print("Lettre trouvée !")
                lettres_trouvées.append(lettre_input)

                if is_win(lettres_trouvées, mot_à_trouver):
                    print("Vous avez gagné ! Le mot était \"" + mot_à_trouver + "\"")
                    response = input('Recommencer (O)ui/(N)on ? ').upper()
                    if response == 'O':
                        nombres_d_erreurs = 0
                        mot_à_trouver = "canard"
                        mot_avec_trou = ""
                        lettres_trouvées = [mot_à_trouver[0]]
                        deja_perdu = False
                    elif response == 'N':
                        pas_fini = False
            else:
                print("Mauvaise lettre !")
                nombres_d_erreurs += 1

