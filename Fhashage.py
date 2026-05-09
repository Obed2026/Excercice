# ==================================================
# 1. DÉFINITION DES FONCTIONS (au début)
# ==================================================

def rotl(x, n, bits=32):
    """Rotation à gauche sur 'bits' bits"""
    n = n % bits
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)

def hash(message):
    
    h = 123456789  # valeur de départ
    for lettre in message:
        code = ord(lettre)
        h = h ^ code           # XOR avec la lettre
        h = rotl(h, 5)         # rotation de 5 bits
        h = h * 1664525        # multiplication
        h = h & 0xFFFFFFFF     # masquage 32 bits
        print(f"Étape intermédiaire : {h}")  
    return f"{h:08x}"          


# ==================================================
# 2. INTERFACE UTILISATEUR (après les fonctions)
# ==================================================

print("=== HACHEUR PERSONNALISÉ ===")
print("Tapez 'quit' pour quitter")

while True:
    message = input("\nEntrez votre message : ")
    if message.lower() == 'quit':
        print("Au revoir !")
        break
    resultat = hash(message)
    print(f"Hash final : {resultat}")
