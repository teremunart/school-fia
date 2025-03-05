Wiederholungsübungen 

(Wenn nicht anders angegeben, beziehen sich die Fragen auf die Tabelle t_posten.) 

 

#### An welchem Datum (TBNr) wurde an den einzelnen Aufträgen gearbeitet (jeder Eintrag soll nur einmal angezeigt werden)? 
````sqlite
    SELECT DISTINCT MIN(TBNr), Aufnr
    FROM t_Posten
    GROUP BY TBNr
    
    -- 2022-02-28,3333
    -- 2022-03-01,4444
    -- 2022-04-02,1111
    -- 2022-11-04,4444

````
#### Wie viele Stunden wurden jeweils an den einzelnen Aufträgen gearbeitet. (Die Auftragsnummer soll auch mit angezeigt werden) 
````sqlite
    SELECT Aufnr, SUM(TStunden)
    FROM t_Posten
    GROUP BY Aufnr
    
    -- 1111,450
    -- 2222,237.5
    -- 3333,231
    -- 4444,85
````

#### Wie hoch ist die Summe der Bonizahlungen von dem Mitarbeiter mit der persnr 8? (Tabelle: t_Bonizahlungen_2021) 
````sqlite
    SELECT SUM(Betrag)
    FROM t_Bonizahlungen_2021
    WHERE Persnr = 8
    
    -- 600
````

#### An wie vielen Tagen wurde an dem Auftrag „4444“ gearbeitet?  
````sqlite
    SELECT COUNT(DISTINCT TBNr)
    FROM t_Posten
    WHERE Aufnr = 4444
    
    -- 4
````
 

#### Wie viele Stunden hat der Mitarbeiter mit der Personalnummer 1 im Februar 2022 an dem Auftrag 4444 gearbeitet?  
````sqlite
    SELECT SUM(Tstunden)
    FROM t_Posten
    WHERE Persnr = 1 AND Aufnr = 4444 AND (TBNr BETWEEN '2022-02-01' AND '2022-02-28')
    
    -- NULL
````

#### An welchen Aufträgen hat der Mitarbeiter mit der Personalnummer 3 gearbeitet? Auch der Tag und die Stundenzahl werden benötigt.  
````sqlite
    SELECT Aufnr, TBNr, Tstunden
    FROM t_Posten
    WHERE Persnr = 3
    ORDER BY TBNr;

    -- 2222,2022-02-28,38
    -- 2222,2022-02-28,12
    -- 1111,2022-02-28,24
    -- 1111,2022-02-28,70
    -- 3333,2022-02-28,12
    -- 3333,2022-02-28,18
    -- 4444,2022-03-01,3
    -- 4444,2022-03-01,4
````
 
#### Geben Sie an, wie oft und mit wie vielen Stunden insgesamt der Mitarbeiter mit der Personalnummer 6 im Feb 2022 an Aufträge gearbeitet hat. Ist es möglich, sich darüber hinaus auch noch die persnr anzeigen zu lassen?  
````sqlite
    SELECT Persnr, COUNT(*) AS WieOft, SUM(TStunden) AS Stunden
    FROM t_Posten
    WHERE Persnr = 3 AND (TBNr BETWEEN '2022-02-01' AND '2022-02-28')

    -- 3,6,174

````

 

8.	Geben Sie das höchste, das kleinste, das durchschnittliche Gehalt und die Summe der Gehaltszahlungen im Januar 2022 an (Tabelle „t_mitarbeitergehalt“).  

 

9.	Welche Mitarbeiter haben im Feb 2022 an den Aufträgen 1111 und 2222 gearbeitet?  

 

10.	Wie viele Stunden sind im  Februar 2022 für die einzelnen Aufträge aufgewendet worden?  

 

11.	Für eine Statistik wird die Untergliederung der in der Tabelle t_Posten für den 01.03.2022 aufgelaufenen Stunden nicht nur nach Auftragsnummer verlangt, sondern auch danach, welcher Mitarbeiter sie geleistet hat. Der besseren Übersicht wegen soll die Anzeige sortiert erfolgen, und zwar aufsteigend nach Auftrags- und Personalnummer.  

Beispielausgabe: 

 

 

 

 

 

 

 

 

 

12.	Welcher Mitarbeiter hat an welchem Auftrag gearbeitet?  

 