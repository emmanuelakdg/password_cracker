import requests
from abc import ABC, abstractmethod

class PasswordCracker(ABC):
    @abstractmethod
    def crack_password(self, password):
        pass
    
    def connexion(password):
        url = 'http://localhost/password_cracker/login.php'

        # Données de formulaire
        data = {
            "login": "admin",
            "password": password,
            "submit": "Login"
        }

        # En-têtes de la requête HTTP
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }

        response = requests.post(
            url,
            data=data,
            headers=headers
        )

        if response.status_code == 200:
            if "Authentification reussie !" in response.text:
                return True
            else:
                return False
        else :
            return False

    