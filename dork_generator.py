# dork_generator.py

def generer_dorks_statiques(domaine):
    dorks = []
    try:
        with open("data/dorks.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
            for ligne in lignes:
                ligne = ligne.strip()
                if ligne:
                    dork = ligne.replace("{domain}", domaine)
                    dorks.append(dork)
    except FileNotFoundError:
        print("[!] Fichier dorks.txt non trouvé. Aucun Dork statique généré.")
    return dorks

def generer_dorks_dynamiques(domaine):
    extensions = ["sql", "env", "log", "json", "conf"]
    mots_cles = ["password", "confidential", "backup", "secret"]
    dyn_dorks = []

    for ext in extensions:
        dyn_dorks.append(f"site:{domaine} ext:{ext}")

    for mot in mots_cles:
        dyn_dorks.append(f"site:{domaine} intext:{mot}")
        dyn_dorks.append(f"site:{domaine} filetype:txt {mot}")

    dyn_dorks.append(f"site:{domaine} intitle:\"index of\"")
    dyn_dorks.append(f"site:{domaine} inurl:admin")
    dyn_dorks.append(f"site:{domaine} inurl:login")
    dyn_dorks.append(f"site:{domaine} inurl:/test/")
    dyn_dorks.append(f"site:{domaine} inurl:robots.txt")

    return dyn_dorks

def generer_tous_les_dorks(domaine):
    return generer_dorks_statiques(domaine) + generer_dorks_dynamiques(domaine)
