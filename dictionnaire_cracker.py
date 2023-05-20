import time
from password_craker import PasswordCracker


class DictionnaireCracker(PasswordCracker):
    def crack_password(self, password):
        with open("dictionnaire.txt", "r") as fichier:
            debut = time.time()
            combinaisons = fichier.read().splitlines()
            if password in combinaisons:
                duree = time.time() - debut
                return True, round(duree,3)
            else:
                duree = time.time() - debut
                return False, round(duree,3)
