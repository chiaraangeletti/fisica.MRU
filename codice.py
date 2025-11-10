#Questo codice richiede i dati di un moto rettilineo uniforme, li esamina, e restituisce ilo tempo, la posizione
#raggiunta in quel tempo e la velocità.

t_iniziale = float(input("Tempo iniziale: "))
t_finale = float(input("Tempo finale: "))
deltaT = float(input("Intervallo di tempo: "))
a = float(input("Accelerazione: "))
v_iniziale = float(input("velocita iniziale: "))
v_finale = float(input("velocita da raggiungere: "))
 
t = t_iniziale
mostrato = 0
 
dati = []
 
while t <= t_finale:
    v = v_iniziale + a * (t - t_iniziale)
    s = v_iniziale * (t - t_iniziale) + 0.5 * a * (t - t_iniziale)**2
 
    dati.append({"tempo": t, "velocita": v, "posizione": s})
 
    print("tempo:", t, "velocita:", v, "posizione:", s)
 
    if mostrato == 0 and v >= v_finale:
        print("velocità di", v_finale, "raggiunta a t =", t)
        mostrato = 1
 
    t = t + deltaT
 
print("risultati")
for punto in dati:
    print(punto)
    
if a > 0:
    print("l'oggetto sta accelerando.")
elif a < 0:
    print("l'oggetto sta rallentando.")
else:
    print("l'oggetto si muove a velocita costante.")
 
 