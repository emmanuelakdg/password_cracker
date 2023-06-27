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
    print("| 1- Connexion par Brute Force                                             |")
    print("| 2- Connexion par Dictionnaire                                                     |")
    print("+-------------------------------------------------------------------------+")

    choix = choisir_option(1, 2)
    if choix == 1:
        brute_force_cracker = PasswordCrackerFactory.create_cracker("brute_force")
        brute_force_cracker.crack_password()
    else:
        dictionnaire_cracker = PasswordCrackerFactory.create_cracker("dictionnaire")
        dictionnaire_cracker.crack_password()

poser_question()