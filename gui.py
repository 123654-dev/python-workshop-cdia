#Importiere die benötigten Bibliotheken
import tkinter as tk

#Eventlistener umgehen, damit alles funktioniert
def onButtonClick():
    global noten_return, checkValue

    noten_return = []

    for i in range(anzahlFächer):
        note = noten[i].get()
        try:
            #Falls LK, dann doppelt
            print(checkValue[i].get())
            if(checkValue[i].get()):
                noten_return.append(int(note))

            noten_return.append(int(note))    
        except:
            print("Note an Stelle " + str(i) + " wurde nicht richtig eingegeben. '" + note +"' ist keine valide Eingabe")

    window.destroy()

def onStart():
    global window, anzahlFächer, noten, fächer, checkboxen, checkValue
    #Erstelle ein neues Fenster
    window = tk.Tk()
    window.title("Zeugniss Rechner")

    #Erstelle die benötigten Variablen
    noten = []
    schnitt = 0
    anzahlFächer = 12

    #Erstelle die benötigten Widgets
    #Erstelle die Labels
    lblFach = tk.Label(window, text="Fach")
    lblNote = tk.Label(window, text="Note")

    #Erstelle die Eingabefelder
    checkValue = [tk.BooleanVar(value=False) for i in range(anzahlFächer)]

    fächer = [tk.Entry(window) for i in range(anzahlFächer)]
    noten = [tk.Entry(window) for i in range(anzahlFächer)]
    checkboxen = [tk.Checkbutton(window, text="LK?", var=checkValue[i]) for i in range(anzahlFächer)]

    #Erstelle den Button
    btnFertig = tk.Button(window, text="Fertig", command=onButtonClick)

    #Positioniere die Widgets
    lblFach.grid(row=0, column=0)
    lblNote.grid(row=0, column=1)

    for i in range(anzahlFächer):
        fächer[i].grid(row=i+1, column=0)
        noten[i].grid(row=i+1, column=1)
        checkboxen[i].grid(row=i+1, column=2)

    btnFertig.grid(row=13, column=1)

#Definiere die Methode zum Auslesen der Noten
def bekommeNoten():
    global window, go, noten_return

    window.mainloop()

    return noten_return

def gebeSchnittAus(schnitt):
    schnitt = str(schnitt)

    fenster = tk.Tk()
    fenster.title("Zeugniss Rechner")
    fenster.geometry("100x50")

    # Erstelle ein Label
    label = tk.Label(fenster, text="Dein Schnitt: "+ schnitt)
    label.pack()

    # Erstelle eine Schleife, damit das Fenster angezeigt wird
    fenster.mainloop()


#Starte GUI beim import
onStart()