# imports
import random

# passwort länge
passwort_laenge = 10

# variablen
i = 0
passwort = ""

# wenn i (bei jeder ascii zahl in zulässiger range incremented) unter passwort länge --> nochmal, bis länge erreicht
while i < passwort_laenge:
    asciiint = random.randint(0, 127)
    if asciiint in range(33, 63) or asciiint in range(65, 89) or asciiint in range(94, 122):
        i += 1
        passwort = passwort + chr(asciiint)

# ausgabe
print("Das Passwort lautet: " + passwort)
