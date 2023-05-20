import hashlib

def calculer_md5(chaine):
    # Crée un objet de hachage MD5
    hachage_md5 = hashlib.md5()

    # Convertit la chaîne en bytes et l'ajoute à l'objet de hachage
    hachage_md5.update(chaine.encode('utf-8'))

    # Récupère la valeur de hachage MD5 sous forme de chaîne hexadécimale
    md5 = hachage_md5.hexdigest()

    return md5

# Exemple d'utilisation
mot_de_passe = "daba"
md5_hash = calculer_md5(mot_de_passe)
print("Le hachage MD5 du mot de passe est :", md5_hash)