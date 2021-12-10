count = 0

print("Bonjour bienvenue sur l'additionneur-3000.")
print("Votre ordinateur peut maintenant réaliser l'exploit d'additionner.")
print("Pour des raisons techniques évidentes, vous êtes limités à 3 essais.")

while (count < 3) :

    print(f"Vous etes actuellement à l'essais : {int(count) + 1}")

    x = int(input("Choisissez un nombre ou chiffre : "))
    y = int(input("Choisissez un second nombre ou chiffre : "))

    print(f"Le résultat de {x} + {y} est égal à : {x + y}")

    count = count + 1

if count == 3:
    print("Merci d'avoir utiliser l'additionneur-3000.")
