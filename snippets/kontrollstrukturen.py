# Code ist an sich eine tolle Sache, aber für alltägliche Anwendungen ist es absolut notwendig, Fälle unterscheiden zu können
# und je nach Situation unterschiedliche Aktionen auszuführen.
# Praktischerweise ist Python mit vielen Kontrollstrukturen ausgestattet, die das auf unterschiedliche Arten ermöglichen.
# if
# if ist die einfachste Kontrollstruktur. Sie prüft, ob eine Bedingung erfüllt ist und führt den Codeblock aus, wenn dies der Fall ist.
# Als Bedingung kann ein Ausdruck stehen, der entweder wahr oder falsch ist.

name = input("Hey! Wie ist dein Name?")
if name == "Umberto":
    print("Hallo Umberto!")

# else
# else ist eine weitere Kontrollstruktur, die verwendet wird, wenn eine spezielle Bedingung nicht erfüllt ist.
# Dann wird ein anderer Codeblock ausgeführt.
# else kann nur verwendet werden, wenn vorher ein if verwendet wurde.

name = input("Hey! Wie ist dein Name?")
if name == "Umberto":
    print("Hallo Umberto!")
else:
    print("Hallo Fremder!")

# elif
# elif ist wie eine Kombination aus if und else. Es wird verwendet, wenn eine Bedingung nicht erfüllt ist, um zu prüfen,
# ob wenigstens eine andere Bedingung erfüllt ist.

name = input("Hey! Wie ist dein Name?")
if name == "Umberto":
    print("Hallo Umberto!")
elif name == "Harald":
    print("Hallo Harald!")
else:
    print("Hallo Fremder!")

# while
# while ist eine Kontrollstruktur, die verwendet wird, um einen Codeblock so lange auszuführen, bis eine Bedingung nicht mehr erfüllt ist.

i = 0
while i < 10:  # ausführen, solange i echt kleiner als 10 ist => aufhören, wenn i 10 ist
    print(i)   # i ausgeben
    i = i + 1  # i um 1 erhöhen

# while funktioniert wie if, allerdings wird der Codeblock nicht genau ein Mal, sondern bis die Bedingung nicht mehr erfüllt ist ausgeführt.

# for
# for ist eine Kontrollstruktur, die verwendet wird, um einen Codeblock für jedes Element in einer Liste auszuführen.

for i in range(10):  # für jedes Element in der Liste range(10) (also für alle Zahlen von 0 bis 9)
    print(i)         # i ausgeben

# for kann auch verwendet werden, um über alle Elemente in einer Liste zu iterieren, d.h. jedes Element der Liste
# einmal in der Variable (hier) name zu speichern und den Codeblock auszuführen.

namen = ["Umberto", "Harald", "Hans"]
for name in namen:
    print(name)

# for kann auch verwendet werden, um über alle Zeichen eines Strings zu iterieren.

name = "Umberto"
for buchstabe in name:
    print(buchstabe)
