import itertools
import os
from password_craker import PasswordCracker

class BruteForceCracker(PasswordCracker):
    def crack_password(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"  # L'alphabet de caractères possibles
        password_length = 6  # La longueur maximale du mot de passe à essayer

        for length in range(1, password_length + 1):
            # Générer toutes les combinaisons possibles de longueur 'length'
            combinaisons = itertools.product(alphabet, repeat=length)

            for combinaison in combinaisons:
                mot = ''.join(combinaison)
                if BruteForceCracker.connexion(mot):
                    print("Connexion reussie avec succes")
                    print(f"Le mot de passe etait: {mot}")
                    return 0
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"patientez...")