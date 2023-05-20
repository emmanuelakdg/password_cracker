from password_craker_factory import PasswordCrackerFactory


def choisir_option(min, max):
    while True:
        choix = input("Entrer votre choix: ")
        try:
            choix_int = int(choix)
        except:
            print("ERREUR!!! Ceci n'est pas un nombre")
        else:
            if not min <= choix_int <= max:
                print(f"OPTION INVALIDE!!! Les options sont compris entre {min} et {max}")
            else:
                return choix_int


def poser_question():
    print("+--------------------------- MENU ----------------------------------------+")
    print("| 1- Cassage par mot de passe                                             |")
    print("| 2- Cassage par Hash                                                     |")
    print("+-------------------------------------------------------------------------+")

    choix = choisir_option(1, 2)
    if choix == 1:
        print("+---------------CASSAGE PAR MOT DE PASSE ---------------------------------+")
        print("| 1- Brute Force                                                          |")
        print("| 2- Dictionnaire                                                         |")
        print("+-------------------------------------------------------------------------+")

        choix1 = choisir_option(1, 2)
        if choix1 == 1:
            password = input("Enter votre mot de passe (max 6 caracteres): ")
            brute_force_cracker = PasswordCrackerFactory.create_cracker("brute_force")
            search, temps, compteur = brute_force_cracker.crack_password(password)
            if search:
                print("Mot de passe trouvé")
                print(f"Cet algorithme a mis {temps}s et a parcouru {compteur} pour trouver ce mot de passe")
            else:
                print("Mot de passe introuvable")
                print(f"Cet algorithme a mis {temps}s pour trouver ce mot de passe")

        else:
            password = input("Entrer votre mot de passe: ")
            dictionnaire_cracker = PasswordCrackerFactory.create_cracker("dictionnaire")
            search, temps = dictionnaire_cracker.crack_password(password)
            if search:
                print("Mot de passe trouvé")
                print(f"Cet algorithme a mis {temps}s pour trouver ce mot de passe")
            else:
                print("Mot de passe introuvable")
                print(f"Cet algorithme a mis {temps}s pour trouver ce mot de passe")
    else:
        print("+---------------------- CASSAGE PAR HASH ---------------------------------+")
        print("| 1- Brute Force                                                          |")
        print("| 2- Dictionnaire                                                         |")
        print("+-------------------------------------------------------------------------+")

        choix2 = choisir_option(1, 2)
        if choix2 == 1:
            password = input("Entrer votre mot de passe (en md5): ")
            hash_brute_force_cracker = PasswordCrackerFactory.create_cracker("hash_brute_force")
            search, temps = hash_brute_force_cracker.crack_password(password)
            if not search == "":
                print(f"Mot de passe: {search}")
                print(f"Cet algorithme a mis {temps}s pour trouver ce mot de passe")
            else:
                print("Mot de passe introuvable")
                print(f"Cet algorithme a mis {temps}s pour trouver ce mot de passe")
        else:
            password = input("Entrer votre mot de passe (en md5): ")
            hash_dictionnaire_cracker = PasswordCrackerFactory.create_cracker("hash_dictionnaire")
            search, temps = hash_dictionnaire_cracker.crack_password(password)
            if not search == "":
                print(f"Votre mot de passe est: {search}")
                print(f"Cet algorithme a mis {temps}s pour trouver ce mot de passe")
            else:
                print("Mot de passe introuvable")
                print(f"Cet algorithme a mis {temps}s pour trouver ce mot de passe")


poser_question()
