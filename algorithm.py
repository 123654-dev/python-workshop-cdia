'''
input: list: notenliste 
output: float: schnitt

Beispielinput: [2,4,2,4,13,12,12,13]
Beispieloutput: 7,56
'''
def berechneSchnitt (notenliste): # notenliste ist ein methodenargument
    summe = 0 # deklariere int variable für Summe der Noten
    for note in notenliste: # Schleife: Für jede Note in einer Liste..
        summe = summe + note # addiere neue note zur bisherigen summe 
    schnitt = summe / len(notenliste) # rechne die summe durch die gesamtanzahl der noten  
    return round(schnitt, 2) # runde auf die letzten 2 Nachkommastellen

def wandleSchnittUm (schnitt):
    #
    # euer code :)
    #
    pass 

print(berechneSchnitt([4,5,6,7,8,9,9,10,10])) # Beispieldurchlauf
