# Eine Funktion ist ein Codeblock, der an anderen Stellen des Programms mehrmals aufgerufen werden kann.
# Dabei wird immer derselbe Code ausgeführt.
# Ein Vorteil ist dabei, dass der Code nicht mehrfach geschrieben oder angepasst werden muss, was die Wartung erleichtert
# und den Code lesbarer macht :D
# Um eine Funktion zu definieren, wird der Schlüsselwort def verwendet.


def hallo():
    print("Hallo Welt!")

# Um eine Funktion auszuführen, wird der Funktionsname mit Klammern, wie er nach dem def steht, aufgerufen.

hallo()

# Eine Funktion kann Parameter enthalten, die beim Aufruf der Funktion übergeben werden können. Das macht Funktionen
# flexibel.

def hallo(name):
    print("Hallo " + name + "!")

hallo("Umberto")
