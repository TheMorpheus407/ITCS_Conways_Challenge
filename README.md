# Conway's Game of Life
## _Code Golf Challenge für den IT Carreer Summit_
### Gewinne eine RTX 3070 TI und vieles mehr

[![N|Solid](https://cdn.clabb.io/evnt/31/itcsonline-wrw0-bg.jpg)](https://clabb.io/de/event/itcsonline)

## Was ist die Aufgabe

Eure Aufgabe ist es, Conways Game of Life zu implementieren.
Frei kopiert von [Wikipedia](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens):
"Das Spiel des Lebens (englisch Conway’s Game of Life) ist ein vom Mathematiker John Horton Conway 1970 entworfenes Spiel, basierend auf einem zweidimensionalen zellulären Automaten. Es ist eine einfache und bis heute populäre Umsetzung der Automaten-Theorie von Stanisław Marcin Ulam."

## Wie teilnehmen?

- Ladet euch von diesem Repository die Dateien `main.py` und `conways_game_of_life.py` herunter
- Fügt euren Code in `conways_game_of_life.py` ein
- Startet die `main.py` mit sowas wie `python main.py --coords 1,2 3,4 5,6 --rounds 2`
    - `--coords` gibt die Koordinaten `x,y` der lebenden Punkte an. Getrennt wird mit einem Leerzeichen zwischen den Punkten und einem Komma zwischen den Koordinaten. Es ist alles 2-dimensional.
    - `--rounds` gibt die Anzahl der Runden an, die ihr simulieren sollt
- Minimiert den Code
    - Wir spielen Code Golf. Hier gewinnt, wer den kürzesten, korrekten Code abliefern kann.
    - Bei Gleichstand gewinnt die durchschnittliche Laufzeit für dieselbe Aufgabe auf meinem Rechner.
- Sendet eure `conways_game_of_life.py` (AUSSCHLIEßLICH DIE!) an [diese Adresse](mailto:kontakt@the-morpheus.de?subject=ITCS%20Challenge%20Abgabe&body=Hallo%20Morpheus%2C%0A%0Amein%20Name%20auf%20clabb.io%2C%20dem%20Portal%20f%C3%BCr%20die%20ITCS%2C%20ist%3A%20%3CNAME%20EINF%C3%9CGEN!!!%3E.%0A%0AMeine%20Datei%20'conways_game_of_life.py'%20findest%20du%20im%20Anhang.%0A%0AIch%20bin%20zur%20Aufl%C3%B6sung%20und%20Siegerehrung%20um%2015%3A30%20sp%C3%A4testens%20wieder%20%20bei%20der%20ITCS%20am%20Start.%0A%0ACheers%2C%0Adein%20Abonnent%0A) und packt euren Namen von Clabb.io dazu! Sonst können wir euch am Ende nicht identifizieren.
- Ihr habt Zeit bis 14:59 einschließlich. Ab 15:00 wird nichts mehr angenommen.

## Wie funktioniert Conways Game of Life?

Das wird [hier](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens#Die_Spielregeln) sehr gut erklärt:
Es gibt tote und lebende Zellen. Zellen sind immer viereckig und haben damit 8 direkte Nachbarn, links, rechts, oben, unten und die 4 Diagonalen. Es wird in Runden gedacht.
- Die toten Zellen fangen in der nächsten Runde an zu leben, wenn in ihrem direkten Umfeld exakt 3 andere Zellen leben.
- Die lebenden Zellen sterben in der nächsten Runde an Einsamkeit, wenn weniger als 2 Zellen in ihrem Umfeld leben, also 1 oder 0.
- Die lebenden Zellen sterben in der nächsten Runde an Überbevölkerung, wenn mehr als 3 Zellen in ihrem Umfeld leben.
- Befinden sich 2 oder 3 lebende Zellen im Umfeld der Zelle, bleibt sie in der nächsten Runde am leben.
> Die Zelle selbst wird nicht mit eingerechnet.
> Eine neue Runde berechnet sich für alle Zellen immer gleichzeitig.
> Eine Visualisierung des Game of Life gibt es [hier.](https://playgameoflife.com/)

## Normalisierung
Bei Conways Game of Life kann es zu "Wanderungen" kommen. Das heißt, sind am Anfang Felder 0,0; 1,0 und 0,1 belegt könnte irgendwann später Feld 1000,1337; 1001,1337 etc belegt sein, jedoch im Bereich 0,0 ist nichts mehr aktiv. Auch in die andere Richtung kann es sich ausbreiten, also mit aktiven Feldern zB auf -10,-20.
Für die Lösung *MÜSSEN* die Ergebnisse normalisiert sein. Für Listen kann es ja keine negativen Einträge geben.
Das bedeutet:
- Ist die Zeile unter 0,x leer, sprich keine einzige Zelle am Leben muss sie gelöscht werden, sodass 1,x zu 0,x wird. Ist 1,x auch leer muss die Zelle ebenfalls gelöscht werden.
- Dasselbe gilt für die Spalte x,0. Auch hier muss x,0 gelöscht werden, wenn keine Zelle dort lebt und x,1 muss an x,0 rücken.
- Sollte die Zelle an -1,x oder x,-1 zum Leben erwachen muss ebenfalls geschoben werden, dieses Mal in die positive Richtung
- Falls es unverständlich war: Es sollte in der obersten Zeile irgendwo eine Zelle leben und in der linkesten Spalte muss auch eine Zelle leben. Negative Indices gehen natürlich ebenfalls nicht

## Q&A
<details>
<summary>Wo kann ich Fragen stellen?</summary>
<br/>
[Hier anfragen.](mailto:kontakt@the-morpheus.de) dann wird es in diesem Readme eingetragen.
</details>
