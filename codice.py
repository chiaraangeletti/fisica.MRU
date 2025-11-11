#Questo codice richiede i dati di un moto rettilineo uniforme, li esamina, e restituisce ilo tempo, la posizione
#raggiunta in quel tempo e la velocità.

#Richiesta dei dati iniziali in input.
t_iniziale = float(input("Tempo iniziale: "))
t_finale = float(input("Tempo finale: "))
deltaT = t_finale-t_iniziale
a = float(input("Accelerazione: "))
v_iniziale = float(input("velocita iniziale: "))
v_finale = float(input("velocita da raggiungere: "))

#Inizializzazione delle variabili di controllo.
t = t_iniziale
mostrato = 0

#Lista per memorizzare i risultati (tempo, velocità, posizione).
dati = []

#Ciclo che simula il moto passo per passo.
while t <= t_finale:
    
    #Calcolodella velocità istantanea (legge del moto 
    #uniformemente accellerato).
    v = v_iniziale + a * (t - t_iniziale)
    
    #Calcolo della posizione istantanea (legge oraria
    #del moto uniformemente accellerato).
    s = v_iniziale * (t - t_iniziale) + 0.5 * a * (t - t_iniziale)**2
 
 #Salvataggio dei dati in una lista di dizionari.
    dati.append({"tempo": t, "velocita": v, "posizione": s})
 
 #Stampa dei valori per ogni intervallo di tempo.
    print("tempo:", t, "velocita:", v, "posizione:", s)
 
 #Controllo della velocità, se la velocità ha raggiunto o superato
 #quella desiderata, viene segnalata solo una volta.   
    if mostrato == 0 and v >= v_finale:
        print("velocità di", v_finale, "raggiunta a t =", t)
        mostrato = 1 #Evita di ripetere la segnalazione.
        
 #Incremento del tempo per il prossimo ciclo.
    t = t + deltaT

#Stampa che riepiloga i risultati memorizzati.
print("risultati")
for punto in dati:
    print(punto)

#Analisi del tipo di moto in base all'accellerazione.
if a > 0:
    print("l'oggetto sta accelerando.")
elif a < 0:
    print("l'oggetto sta rallentando.")
else:
    print("l'oggetto si muove a velocita costante.")
 
 