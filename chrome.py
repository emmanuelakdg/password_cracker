
from selenium import webdriver

url = "https://localhost/password_cracker/login.php"  # Remplacez cette URL par celle que vous souhaitez ouvrir

# Spécifiez le chemin vers le pilote Chrome WebDriver que vous avez téléchargé
webdriver_path = "/chemin/vers/le/pilote/chrome/webdriver"

# Configuration du pilote Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Ouvrir Chrome en mode maximisé (plein écran)

# Instanciation du pilote Chrome WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

# Ouvrir l'URL spécifiée dans Chrome
driver.get(url)
