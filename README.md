# 🦾 ***fisica.MRU*** 🚀

## 📃 Indice
- [Descrizione](#descrizione)
- [Sviluppo del codice](#sviluppo-del-codice)
- [Strategia](#strategia)
- [Autori](#autori)

## ✒️ Descrizione

In questo progetto abbiamo studiato il moto uniformemente accelerato (MUA), cioè un tipo di movimento in cui la velocità di un corpo varia in modo costante nel tempo.
In altre parole, l’accelerazione rimane sempre uguale, e ciò significa che ad ogni intervallo di tempo la velocità aumenta (o diminuisce) della stessa quantità.
Lo scopo principale del lavoro è stato quello di creare un programma in grado di simulare un esperimento di moto uniformemente accelerato, simile a quelli che si possono svolgere in laboratorio di fisica.
Il programma:
• richiede in input alcuni dati fondamentali come il tempo iniziale, il tempo finale, l’intervallo di tempo, l’accelerazione e la velocità iniziale;
• calcola la velocità e lo spostamento del corpo in ogni istante considerato;
• determina il momento preciso in cui si raggiunge una certa velocità stabilita dall’utente;
• infine, restituisce una tabella di valori o un output testuale che mostra l’evoluzione del moto nel tempo.
L’obiettivo didattico del progetto è comprendere in modo più intuitivo come si comporta un corpo soggetto a un’accelerazione costante, trasformando le formule del moto in un’esperienza interattiva e visuale.

## 🧠 Sviluppo del codice

- *Il codice deve richiedere in input il tempo iniziale: t0 (t con zero), il tempo finale: t, l'intervallo di tempo, l'accellerazione: a, e la velocità iniziale: V0 (V con zero).*
- *Calcolare V (velocità) e s (spostamento) ad ogni intervallo di tempo con cicli for o while.*
- *Salvare i risultati di velocità e spostamento in una lista e dizionari.*
- *Restituire il tempo in cui si raggiunge una certa velocità con la condizione if.*
- *Restituire una tabella di dati o un testo.*
- *Si può usare ChatGPT ma si deve saper spiegare il procedimento.*

## ⚙️ Strategia

Il programma utilizza diverse strategie per descrivere il moto di un oggetto. Inizialmente vengono raccolti i dati necessari dall’utente, come tempo, accelerazione e velocità iniziale e finale. Successivamente, un ciclo incrementa il tempo con piccoli intervalli costanti, simulando il movimento passo dopo passo e calcolando a ogni intervallo la velocità e la posizione dell’oggetto mediante le formule del moto uniformemente accelerato.
I valori calcolati vengono memorizzati in una lista di dizionari, in modo da poterli visualizzare o analizzare al termine dell’esecuzione. Viene inoltre eseguito un controllo che segnala il momento in cui la velocità raggiunge o supera quella finale, evitando ripetizioni del messaggio. Infine, il programma verifica il segno dell’accelerazione per determinare se l’oggetto sta accelerando, rallentando o mantenendo una velocità costante.
 
## 🖍️ Autori
Angeletti Chiara - Pausini Giacomo - Ramaccioni Matteo - Stramaccioni Tommaso
