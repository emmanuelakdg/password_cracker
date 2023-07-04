import os
from password_craker import PasswordCracker


class DictionnaireCracker(PasswordCracker):
    def crack_password(self):
        with open("dictionnaire.txt", "r") as fichier:
            combinaisons = fichier.read().splitlines()
            for password in combinaisons:
                if DictionnaireCracker.connexion(password):
                    print("Mot de passe trouvé : ", password)
                    return 0
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("patientez...")
        
        print("Le mot de passe n'existe pas dans le fichier")

