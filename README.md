# Stima delle proprietà dei cristalli di Silicio (Si)

Questo file dovrebbe fungere da diario di bordo.  
Qui raccolgo pensieri, dubbi e problemi.  
L'idea è di raccogliere in un unico luogo i vari esempi della Boeri.  
La prima cosa da notare è che ODIO il fatto che lei abbia sempre messo tutti i file in un'unica cartella --> cerchiamo di fare più ordine.

Struttura delle cartelle:
```  
Si/  
│  
├── data/        # qui raccolgo eventuali dati elaborati  
├── input/       # file di input per quantum espresso  
├── output/      # file di output di quantum espresso  
├── pseudo/      # cartella per pseudopotenziali  
├── tmp/         # qui quantum espresso salva i suoi file interni  
├── util/        # altri codici utili per elaborare i dati  
├── README.md    # questo file  
└── makefile     # makefile  
```
Per il momento le cartelle data e util sono vuote, andrò a popolarle quando avrò creato degli script che siano utili per analizzare i dati.

## Introduzione

Voglio stimare le proprietà di un cristallo di Si utilizzando quantum espresso (qe).  
Esistono più strutture possibili per il Si --> mi concentrerò sulla struttura a diamante.  
Reference: [materials project](https://next-gen.materialsproject.org/materials/mp-149?chemsys=Si)

## Struttura del calcolo

Gli step da seguire dovrebbero essere i seguenti:
- stabilire come è fatta la cella (relaxation)
- trovare gli orbitali (scf e nscf)
- trovare bande e dos (post processing)

Mi interessano altre proprietà --> boh  
Fononi? Tensore polarizzabilità/conduzione?  
Se mi interessassero, come li trovo? --> boh

## Relaxation

Non mi è del tutto chiaro che differenza ci sia tra `relax` e `vc-relax`.  
Mi pare di capire che `relax` trova la posizione degli atomi all'interno della cella, mentre `vc-relax` fa variare la dimensione e forma della cella.  
Per quale motivo dovrei fare le due cose separatamente? --> boh  

Ci aspettiamo che il Si cristallizzi in una struttura a diamante.  
Questo corrisponde a un FCC (ibrav = 2) con base.  
Ci aspettiamo un parametro reticolare pari a 5.44 Å = 10.280109378 Bohr.  
(NOTA: il parametro celldm va indicato in bohr!)

### relax

Inserisco un parametro di partenza celldm = 10.40 e delle posizioni atomiche diverse da quelle che mi aspetto --> voglio vedere se qe riesce correttamente a partire da questa lunghezza e raggiungere quella corretta.  
Ho ripetuto questo metodo più volte, e giustamente quando i valori che assegnavo erano troppo lontani da quelli attesi, il calcolo non convergeva mai.  
Mi sembra interessante lavorare comunque con valori piuttosto distanti da quelli attesi --> questo mi permette di avere molti dati (inutili) nell'output, e di vedere come ragiona qe.

Le posizioni trovate sono:
```
ATOMIC_POSITIONS (alat)
Si               0.1000277107       -0.0000000000       -0.0000000000
Si               0.3499722893        0.2500000000        0.2500000000
End final coordinates
```
Questa geometria è praticamente identica a quella attesa, solo che tutto è traslato lungo x!  
Mi piacerebbe poter richiedere che i calcoli vengano svolti mantenendo un atomo fisso, e facendo variare l'altro --> finchè ho solo 2 atomi nel cristallo mi sembra un modo di lavorare simpatico, ma non so se si possa fare  
TODO: potrebbe essere utile fare uno script che legge i vari dati (tipo energia, posizione atomi, forze tra atomi) dall'output di quantum espresso, per vedere come si evolvono nelle varie interazioni e fare un plot che dimostra che ho raggiunto la convergenza --> per ora ho confrontato i dati ad occhio

### vc-relax

In questa fase facciamo variare i parametri della cella.  
Prenderò per buona la posizione iniziale degli atomi che ho trovato nel punto precedente, ovvero:
```
ATOMIC_POSITIONS  
Si   0.00   0.00   0.00  
Si   0.25   0.25   0.25  
```
Farò partire la simulazione da celldm(1) = 11, e mi aspetto che converga a 10.28 BOHR (5.44 Å).

I valori che ottengo alla fine sono:
```
CELL_PARAMETERS (alat= 11.00000000)  
  -0.464352239  -0.000000000   0.464352239  
   0.000000000   0.464352239   0.464352239  
  -0.464352239   0.464352239  -0.000000000  

ATOMIC_POSITIONS (alat)  
Si              -0.0000000000       -0.0000000000       -0.0000000000  
Si               0.2321761197        0.2321761197        0.2321761197  
```
La posizione dell'atomo si discosta da 0.25 e il nuovo parametro di cella dovrebbe essere 10.215749258 bohr.  
Questi valori sono diversi dai valori attesi, ma per il momento mi ritengo soddisfatto --> penso di esserci andato abbastanza vicino.

## Calcolo orbitali

A questo punto provo a calcolare gli orbitali, dando per buoni i parametri calcolati nello step precedente.  
Sarebbe in realtà utile fare un'analisi dei dati forniti nei 2 step precedenti --> posso ritenermi veramente soddisfatto di questi dati? ho avuto una vera convergenza, o mi servono dei calcoli più precisi?  
Per il momento non risponderò a queste domande --> Il mio scopo per ora è solo di capire un po' meglio il funzionamento di qe

### scf

Il primo step per calcolare gli orbitali è un calcolo che risolva le equazioni auto consistenti.  
Questo calcolo è decisamente più pesante del successivo, ma è anche più rigoroso.  
Come posso confrontare questi dati con qualche reference? --> Non lo so  

### nscf

Questo è un calcolo non auto consistente, e quindi più leggero.  
Questo mi permette di aumentare il numero di k points da usare, per ottenere un risultato più preciso.  
Sarebbe sensato che questo calcolo sfruttasse i dati ottenuti dallo step precedente, ma è davvero così? --> non mi è chiaro, ma credo di si  
L'output di qe è un po' diverso dallo step precedente, ma credo che sia tutto in ordine.  
Ancora una volta: come posso confrontare questo output con una reference? --> non lo so

## Post processing

Qui dobbiamo fare 3 cose:
- ricavare la densità elettronica
- ricavare la struttura a bande
- ricavare la densità di stati

### densità di carica

Eseguendo il comando ottengo 2 file: il file `.xsf` può essere aperto in VESTA, ma non so a cosa serva il file `.out`.  
Ho aperto il file `.xsf` in VESTA, ma come faccio a capire se ho ottenuto un risultato ragionevole? --> boh  
Come chiedo a VESTA di usare la cella convenzionale? --> boh  

### bande e dos

Questo calcolo si articola in 2 fasi.  
Nella prima fase usiamo `pw.x` per calcolare le bande.  
Ho preso i k points da [qui](https://www.vasp.at/wiki/index.php/KPOINTS), e spero che siano corretti.  
Proverò con:
```
 K_POINTS (crystal_b)
5
0.00   0.00   0.00   40   ! Γ
0.50   0.50   0.00   40   ! X
0.50   0.75   0.25   40   ! W
0.375  0.375  0.75   40   ! K
0.00   0.00   0.00   40   ! Γ
```
Nella seconda fase possiamo usare `bands.x` e `dos.x` per calcolare la struttura a bande e la densità di stati.  
Sicuramente è necessario calcolare le bande con `pw.x` prima di usare `bands.x`, ma è uno step necessario anche per poter usare dos.x? --> non lo so ma credo di sì.  
L'output di `bands.x` contiene numerosi file, ma non so come interpretarli tutti.  
Per ora consideriamo solo il file `.gnu`.

## Plot

Per plottare i dati ho usato gli scripts che si trovano in `util/`  
Questi script sono quelli forniti dalla prof con minime modifiche --> andranno aggiornati!  
In particolare vorrei capire come assegnare correttamente i nomi dei k points lungo l'asse x nel grafico delle bande.  
Il risultato finale mi sembra ragionevole (?), ma non ne sono sicurissimo --> dovrei confrontarlo meglio con la reference.