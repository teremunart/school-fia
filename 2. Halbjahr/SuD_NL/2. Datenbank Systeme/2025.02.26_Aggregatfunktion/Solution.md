## Aggregat- Rechen- und Datumsfunktionen
(Wenn nichts anderes steht, beziehen sich die Abfragen auf „t_Personaldaten“). Jede Frage soll mit einem Statement gelöst werden.

#### Ermitteln Sie mithilfe einer Aggregatfunktion das durchschnittliche Eintrittsgehalt.
```sqlite
    SELECT AVG(Eintrittsgehalt)
    FROM t_Personaldaten

    -- AVG = 3000    
```
#### Zu welchem Datum trat der erste Angestellte bei?
````sqlite
    SELECT MIN(Eintritt)
    FROM t_Personaldaten

    -- 1998-02-01
````
#### Lassen Sie sich den Namen dieses/r Mitarbeiter/s anzeigen.
````sqlite
    SELECT Pname, PVorname, Eintritt
    FROM t_Personaldaten
    WHERE Eintritt = (SELECT MIN(Eintritt) FROM t_Personaldaten)

    -- Schaefer Johanna
````
#### Wer hatte das höchste und wer das niedrigste Eintrittsgehalt?
````sqlite
    SELECT Pname, PVorname, Eintrittsgehalt
    FROM t_Personaldaten
    WHERE Eintrittsgehalt = 
       (SELECT MIN(Eintrittsgehalt) FROM t_Personaldaten)
    OR Eintrittsgehalt = 
       (SELECT MAX(Eintrittsgehalt) FROM t_Personaldaten)

    -- Eifer,Stefan,4500
    -- Franzke,Axel,4500
    -- Zeiss,Gisela,2700


````
#### Wie viele Mitarbeiter hat die Firma?
````sqlite
    SELECT COUNT(*)
    FROM t_Personaldaten
    
    -- COUNT = 8
````
Wie viele männliche und wie viele weibliche Mitarbeiter hat die Firma?
````sqlite
    SELECT
        COUNT(CASE WHEN Geschlecht = 'M' THEN 1 END) AS males,
        COUNT(CASE WHEN Geschlecht = 'W' THEN 1 END) AS females
    FROM t_Personaldaten;

    -- males = 5, females = 2

````
#### An wie vielen unterschiedlichen Terminen wurden Einstellungen vorgenommen?
````sqlite
    SELECT COUNT(DISTINCT Eintritt)
    FROM t_Personaldaten
    
    -- COUNT = 7
````
#### Wie viele Mitarbeiterinnen gibt es und wie hoch ist ihr Durchschnitteintrittsgehalt?
````sqlite
    SELECT COUNT(*), AVG(Eintrittsgehalt)
    FROM t_Personaldaten
    
    -- COUNT = 8, AVG = 3800
````
#### Wie viele Mitarbeiter arbeiten jeweils in einer Abteilung?
````sqlite
    SELECT Abtnr, COUNT(Abtnr)
    FROM t_Personaldaten
    GROUP BY Abtnr
    
    -- 1,2
    -- 2,2
    -- 3,2
    -- 4,2
````
#### Wie viele Familienmitglieder hat der Mitarbeiter „Tom Meier“ (bezogen auf die Tabelle t_Familienmitglieder) und wie hoch beläuft sich die Summe der Zuschläge? (Die Personalnummer ist nicht bekannt)
````sqlite
    SELECT COUNT(*), SUM(Zuschlag)
    FROM t_Familienmitglieder
    WHERE Persnr = (
        SELECT Persnr 
        FROM t_Personaldaten 
        WHERE PVorname = 'Tom' AND PName = 'Meier'
    )
    
    -- 3, 160
````
#### Wie oft wurde der Smart Fortwo, Kennzeichen 'K-QM-281', gemietet.
````sqlite
    SELECT COUNT(*)
    FROM Mietvorgang
    WHERE Auto = (
        SELECT Auto_ID
        FROM Autos WHERE Nummernschild = 'K-QM-281'
    )
    
    -- 2
````
#### Wie viele Tage liegen zwischen dem 01.02.1980 und 15.05.1985? (Funktioniert nicht in SQLite)
> EMPTY
#### Der Mitarbeiter 'Franzke’mit der Personalnummer 5 will wissen, wie viele Tage er nach dem Mitarbeiter Eifer mit der Personalnummer 1 in das Unternehmen eingetreten ist. (Funktioniert nicht in SQLite)
> EMPTY 

#### Wie oft hat sich Frau Zeiss im Jahr 2021 ein Auto ausgeliehen?
````sqlite
    SELECT COUNT(*)
    FROM Mietvorgang
    WHERE Mitarbeiter_ID = (
        SELECT Persnr 
        FROM t_Personaldaten 
        WHERE PName = 'Zeiss'
    )
    
    -- 0
````

#### Welche Mitarbeiter wurden im März 1984 eingestellt?
````sqlite
    SELECT PVorname, PName 
    FROM t_Personaldaten
    WHERE Eintritt BETWEEN '1984-03-01' AND '1984-03-31'
    
    -- None
````
		


		


		



