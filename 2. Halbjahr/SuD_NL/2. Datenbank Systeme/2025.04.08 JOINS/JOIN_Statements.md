### 1.
````sqlite
SELECT t_Personaldaten.Persnr, PName, Vorname
FROM t_Personaldaten JOIN t_Familienmitglieder
WHERE t_Personaldaten.Persnr = t_Familienmitglieder.Persnr
ORDER BY t_Personaldaten.Persnr DESC
````

### 2.
````sqlite
SELECT Persnr, PName, 
    (SELECT Vorname 
     FROM t_Familienmitglieder 
     WHERE t_Familienmitglieder.Persnr = t_Personaldaten.Persnr) AS Vorname
FROM t_Personaldaten
ORDER BY Persnr DESC;
````

### 3.
````sqlite
SELECT PName, MGehalt
FROM t_Personaldaten JOIN t_Mitarbeitergehalt
WHERE MGehalt<4000 AND Monat=1 AND Jahr=2021;
````

### 4.
````sqlite
SELECT t_Personaldaten.Persnr, PName, Vorname
FROM t_Personaldaten JOIN t_Familienmitglieder
WHERE t_Personaldaten.Persnr = t_Familienmitglieder.Persnr
ORDER BY t_Personaldaten.Persnr DESC
````