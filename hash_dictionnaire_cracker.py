import time
import hashlib
from password_craker import PasswordCracker


class HashDictionnaireCracker(PasswordCracker):
    def crack_password(self, password_hash):
        debut = time.time()
        with open("dictionnaire.txt", "r") as fichier:
            combinaisons = fichier.read().splitlines()
            for combinaison in combinaisons:
                hachage_md5 = hashlib.md5()
                hachage_md5.update(combinaison.encode('utf-8'))
                md5 = hachage_md5.hexdigest()
                if md5 == password_hash:
                    duree = time.time() - debut
                    return combinaison, round(duree,3)

        duree = time.time() - debut
        return "", round(duree,3)
