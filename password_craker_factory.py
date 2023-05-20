from brute_force import BruteForceCracker
from dictionnaire_cracker import DictionnaireCracker
from hash_brute_force_craker import HashBruteForceCracker
from hash_dictionnaire_cracker import HashDictionnaireCracker


class PasswordCrackerFactory:
    @staticmethod
    def create_cracker(cracker_type):
        if cracker_type == "brute_force":
            return BruteForceCracker()
        elif cracker_type == "dictionnaire":
            return DictionnaireCracker()
        elif cracker_type == "hash_brute_force":
            return HashBruteForceCracker()
        elif cracker_type == "hash_dictionnaire":
            return HashDictionnaireCracker()
        else:
            raise ValueError("Invalid cracker type.")
