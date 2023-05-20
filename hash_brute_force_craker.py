import time
import itertools
import hashlib
from password_craker import PasswordCracker

class HashBruteForceCracker(PasswordCracker):
    def crack_password(self, password_hash):
        debut = time.time()
        alphabet = "abcdefghijklmnopqrstuvwxyz"  # L'alphabet de caractères possibles
        taille_password = 6  # La longueur maximale du mot de passe à essayer
        trouver = ""

        for taille in range(1, taille_password + 1):
            # Générer toutes les combinaisons possibles de longueur 'taille'
            combinations = itertools.product(alphabet, repeat=taille)

            for combination in combinations:
                mot = ''.join(combination)

                # Crée un objet de hachage MD5
                hachage_md5 = hashlib.md5()

                # Convertit la chaîne en bytes et l'ajoute à l'objet de hachage
                hachage_md5.update(mot.encode('utf-8'))

                # Récupère la valeur
                #  de hachage MD5 sous forme de chaîne hexadécimale
                md5 = hachage_md5.hexdigest()

                if md5 == password_hash:
                    duree = time.time() - debut
                    return mot, round(duree,3)
        duree = time.time() - debut
        return "", round(duree,3)