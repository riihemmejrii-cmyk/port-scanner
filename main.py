import socket

cible = input("Entrez l'adresse IP ou le nom d'hôte : ")
port_debut = 1
port_fin = 1024

print(f"\nScan de {cible} en cours...")
print("-" * 40)

for port in range(port_debut, port_fin + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    resultat = sock.connect_ex((cible, port))
    if resultat == 0:
        print(f"Port {port} : OUVERT")
    sock.close()

print("-" * 40)
print("Scan terminé !")
