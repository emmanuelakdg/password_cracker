from BruteForceConnexion import BruteForceCracker
from dictionnaire_cracker import DictionnaireCracker



class PasswordCrackerFactory:
    @staticmethod
    def create_cracker(cracker_type):
        if cracker_type == "brute_force":
            return BruteForceCracker()
        elif cracker_type == "dictionnaire":
            return DictionnaireCracker()
        else:
            raise ValueError("Invalid cracker type.")
