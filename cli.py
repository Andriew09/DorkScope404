# cli.py
from dork_generator import generer_tous_les_dorks

def menu_principal():
    while True:
        print("\n=== DorkScope CLI ===")
        print("1. Générer des Dorks")
        print("2. Quitter")
        
        choix = input("Choisissez une option : ")

        if choix == "1":
            domaine = input("Entrez le domaine (ex : facebook.com) : ")
            dorks = generer_tous_les_dorks(domaine)
            print("\nDorks générés :\n")
            for dork in dorks:
                print(dork)
        elif choix == "2":
            print("Au revoir!")
            break
        else:
            print("[!] Option invalide. Essayez à nouveau.")

if __name__ == "__main__":
    menu_principal()
