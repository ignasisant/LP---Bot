Practica Python - Skline Telegram Bot
------------------------------------------------------------------------------------
Carpetes:
L'arxiu de la pràctica conté dues carpetes
1. botFolder : Conté tot el que fa referència al bot , els gràfics , la gestió de memòria i la comunicació entre els diferents elements. En aquesta carpeta trobem:

- bot.py -> programa principal del bot(haurem d'executar-lo per a que el bot funcioni).
- Handlers.py -> conté tots els Handlers necessaris per a fer funcionar el bot.
- Estat.py -> conté tots els mètodes que fan que les comandes entrades per l'usuari tinguin un efecte real, també s'encarrega de la comunicació entre els diferents elements que componen la Pràctica.
- Skyline.py -> S'encarrega de la gestó dels skylines, com ara la generació del skyline random, garantir la relació entre skyline i identificador d'aquest, etz.
- Grafics.py -> Conté tots els mètodes que permenten generar les figures que representen els skylines.
- GestorSkylines.py -> S'encarrega de la gestió de memoria (save/load).
- token.txt -> token del bot (per si de cas)
- adreça.txt -> adreça del bot

2. cl : Conté tot els arxius que fan referència a la gramàtica que usarem per dibuixar els Skylines. En aquesta carpeta hi trobem:

- Skyline.g -> Gramàtica que accepta el bot.
- SkylineLexer.py -> Lexer de la gramàtica.
- SkylineParser.py -> Parser de la gramàtica
- SkylineVisitor.py -> Visitor de la gramàtica, extreu les dades del que l'usuari entra al bot per tal de crear els Skylines
- Altres : altres arxius no rellevants
 
Us:
Per executar aquest Bot es pot usar la seguent comanda des de dins de la carpeta 'botFolder':

python3 bot.py

----------------------------------------------------------------------------
Per tal de fer el bot hi ha basicament tres parts a tractar:
-El bot
-Figura del Skyline
-La Gramàtica i les operacions
------------------------------------------------------------------------------------
EL BOT
Per tal d'implementar el bot m'he basat en els tutorials de la propia pàgina de LP. Amb la comanda /help es pot veure totes les comandes disponibles. 
El bot funciona encara que no introdueixis la comanda /start.
Basicament el que fa el bot és llegir les comandes introduides i si és una de les que te definit un Handler aplica el mètode associat a aquest.
Si no és així passa la comanda a la gramàtica per tal d'analitzar el seu contingut. Si la gramàtica no enten la comanda el bot mostrarà per pantalla un missatge d'error.
Quan tot funciona correctamanet el bot usa el mètode "sendPhotoBuffer" per enviar la figura que representa el skyline i el mètode "sendMessage" per enviar els missatges que corresponen a l'area i l'alçada. Aquest últim mètode el reúsarem per a que el bot mostri per pantalla tots els missatges que vulguem.
Per enviar la figura de l'skyline usem buffers ja que és la millor manera de fer-ho ja, aixi les dades s'enmagatzemen de manera temporal.
El bot fa bé totes les comandes menys save/load que depenent de quina situació hi ha algun error que no he tingut temps d'arreglar.

----------------------------------------------------------------------------------

FIGURA DEL SKYLINE

En aquest treball s'ha definit que un skyline és un conjunt d'edificis, i un edifici es representa amb un Array de ints [xmin,h,xmax] fent que un skyline sigui una matriu de int.

Per tal de computar la figura del skyline usem la classe "Grafics" de l'arxiu Grafics.py aquesta usa el mètode "pintaGrafic" que rep un skyline com a parametre i dibuixa els seus edificis. Un cop te el gràfic fet usa el mètode privat "__get_grafic_buffer" per tal d'introduir el gràfic en un baffer que s'usarà per més tard llegir el seu contingut i mostrar-lo en la conversació del bot. He optat per usar un buffer ja que és la millor opció per guardar el la figura temporalment fins que l'enviem per al bot. En aquesta classe també calculem l'area i l'alçada del skyline .

------------------------------------------------------------------------------------

GRAMÀTICA I OPERACIONS

La gramàtica d'aquesta pràctica s'ha fet pensant en les operacions que s'haurien de poder fer.  En l'arxiu Skyline.g hi trobem les regles. Les variables només poden ser combinacions de lletres (minuscula o majuscula).
El visitor de la gramàtica extreu tota la informació del que li arriba i classifica aquesta tal i com s'ha definit en les regles. Hi ha certes operacions que es fan directament en el visitor. Entre aquestes hi tobem: els desplaçaments (mètode desplaca()) , mirall (mètode gira()) , replicació (mètode repeteix()) i la unió (metode unio()). 

Per fer la unió basicament el que he fet és una matriu de mida (xmax_maxim-xmin_minim) * altura_maxima_ (ES UN SKYLINE GIRAT on els edificis creixen cap a les columnes amb major valor). Aquesta matriu s'inicialitza tota a 0 i representa cada una de les unitats on hi pot haver un edifici o no . Per fer la unió el mètode rep dos skylines, omple la matriu amb el mètode (omple_mat()) i finalment extreu el resultat de la unió amb el mètode extreu_resultat_unio().
per exemple si tenim un skyline [0,2,2] i un altre [0,1,3] despres d'omplir la matriu tindriem:

[2, 1] -> skyline girat 90º en sentit de les agulles del rellotge
[2, 1]
[1, 0] Com veiem tampoc contem els edificis d'altura 0 ja que no formen part de la matriu.


A grans trets el que fan aquests mètodes és traduir un skyline a matriu, això ho fem sumant 1 a les posicions on hi hauria un edifici, per tant si a la posició hi ha un valor més gran de 0 vol dir que al fer la unió haurem de tindre en compte aquell edifici. Pot ser que en alguna casella de la matriu hi hagi un valor superior a 1 això serà perque hi ha més d'algun edifici que se solapa en aquell punt. Aquesta matriu la podem reúsar per fer la intersecció ja que en comptes de mirar quines posicions tenen un valor més gran que 0 mirariem quines posicions tenen valor 2 (tenint en compte que en cap dels skylines d'entrada hi ha solapacions). 
Finalment per extreure els edificis resultants de la unió, anirem recorrent la matriu. Per trobar xmin d'un edifici haurem de mirar si a la columna 0 hi ha un valor més gran que 0 , si és aixi prendrem el valor d'aquella fila (mes xmin_minima_ del skyline per no fer un desplaçament) com a xmin, un cop tenim xmin haurem de buscar el últim valor de la fila que conté un 1 , que serà l'altura de l'edifici (sumem 1 ja que edificis d'altura 0 no els contem). Un cop tenim l'altura de l'edifici haurem de mirar si a la següent fila hi ha un altres valors més grans que 0 arriben a la mateixa altura. Si és aixi encara no definirem xmax. Per altre banda si l'altura varia haurem de tancar l'edifici i pertant declararem xmax com el nombre de la fila (més xmin_minima_ del skyline per no provocar un desplaçament). Quan ja tenim xmin, l'altura i xmax ja podem definir un nou edifici, i després podem buscar el següent. Sempre que busquem l'altura i la xmax haurem de tenir en compte les dimensions de la matriu ja que pot ser l'edifici més alt o l'ultim edifici.

La intersecció no la he fet per falta de temps pero un cop tenint aquesta matriu és ben senzill ja que només hem de crear els edificis tenint en compte en quines posicions hi ha valor 2 , i que pertant hi ha solapament. Podem reusar bona part del codi ja fet.


















