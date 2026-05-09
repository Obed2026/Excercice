Exercice/
├── Fhashage.py    # Code source principal
└── README.md      # Documentation
Mon fichier d'Hashage
Tapez 'quit' pour quitter

Entrez votre message : Hello
Étape intermédiaire : 825373492
Étape intermédiaire : 3289675431
Étape intermédiaire : 123456789
Étape intermédiaire : 2987654321
Étape intermédiaire : 987654321
Hash final : 3ade68b1

Entrez votre message : quit
Au revoir 
Départ : h = 123456789
           
1. XOR avec 'A' (65) : h = 123456789 ^ 65 = 123456788
           
2. Rotation gauche 5 bits : les bits tournent
           
3. Multiplication par 1664525 : h devient grand
           
4. Masque & 0xFFFFFFFF : garde 32 bits
           
5. Formatage : transforme en "075bcd15" (exemple)
