import time
import itertools
from password_craker import PasswordCracker


class BruteForceCracker(PasswordCracker):
    def crack_password(self, password):
        debut = time.time()
        alphabet = "abcdefghijklmnopqrstuvwxyz"  # L'alphabet de caractères possibles
        taille_password = 6  # La longueur maximale du mot de passe à essayer
        trouver = False
        compteur = 0

        for taille in range(1, taille_password + 1):
            # Générer toutes les combinaisons possibles de longueur 'taille'
            combinaisons = itertools.product(alphabet, repeat=taille)

            for combinaison in combinaisons:
                mot = ''.join(combinaison)
                compteur+=1 
                # Vérifier si le mot de passe est correct (remplacez cette condition par votre propre vérification)
                if mot == password:
                    duree = time.time() - debut
                    return True, round(duree,3), compteur
        duree = time.time() - debut
        return trouver, round(duree,3), compteur
