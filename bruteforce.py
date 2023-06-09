import itertools
from password_craker import PasswordCracker

class BruteForceCracker(PasswordCracker):
    def crack_password(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"  # L'alphabet de caractères possibles
        password_length = 6  # La longueur maximale du mot de passe à essayer
        passwords = []

        for length in range(1, password_length + 1):
            # Générer toutes les combinaisons possibles de longueur 'length'
            combinaisons = itertools.product(alphabet, repeat=length)

            for combinaison in combinaisons:
                mot = ''.join(combinaison)
                passwords.append(mot)

        return passwords
