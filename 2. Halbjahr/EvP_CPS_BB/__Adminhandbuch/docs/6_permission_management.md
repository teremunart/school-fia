# Rechte in Linux

---

## Inhaltsverzeichnis
- [Dateirechte verstehen](#dateirechte-verstehen)
- [Befehle zur Verwaltung von Rechten](#befehle-zur-verwaltung-von-rechten)
  - [chown](#chown)
  - [chmod](#chmod)
  - [ls -l](#ls-l)
- [Berechnung der Berechtigungen](#berechnung-der-berechtigungen)

---

## Dateirechte verstehen

In Linux gibt es drei Arten von Berechtigungen:

| Berechtigung    | Beschreibung                                           |
|-----------------|--------------------------------------------------------|
| `Lesen (r)`     | Berechtigung, die Datei zu lesen.                      |
| `Schreiben (w)` | Berechtigung, die Datei zu bearbeiten oder zu löschen. |
| `Ausführen (x)` | Berechtigung, die Datei als Programm auszuführen.      |


Die Berechtigungen werden in drei Gruppen unterteilt:

| Typ        | Beschreibung                                        |
|------------|-----------------------------------------------------|
| `Besitzer` | Der Benutzer, der die Datei erstellt hat.           |
| `Gruppe`   | Die Benutzer, die zur Gruppe des Besitzers gehören. |
| `Andere`   | Alle anderen Benutzer.                              |

Das Format `drwxr-xr--` gibt die Berechtigungen für eine Datei oder ein Verzeichnis an:
- Das erste Zeichen `d` zeigt an, ob es sich um ein Verzeichnis `d` oder eine Datei `-` handelt.
- Die nächsten drei Zeichen `rwx` zeigen die Berechtigungen für den Besitzer an.
- Die nächsten drei Zeichen `r-x` zeigen die Berechtigungen für die Gruppe an.
- Die letzten drei Zeichen `r--` zeigen die Berechtigungen für andere Benutzer an.

> ### Beispiel:
> - `drwxr-xr--` <br>
|→ `d`: Verzeichnis <br>
|→ `rwx`: Der Besitzer hat Lese-, Schreib- und Ausführungsrechte. <br>
|→ `r-x`: Die Gruppe hat Lese- und Ausführungsrechte, aber kein Schreibrecht. <br>
|→ `r--`: Andere Benutzer haben nur Lesezugriff.

---

## Befehle zur Verwaltung von Rechten

### chown
Mit dem Befehl `chown` kannst du den Besitzer und die Gruppe einer Datei oder eines Verzeichnisses ändern:
```bash
sudo chown NEUER_BESITZER:NEUE_GRUPPE DATEINAME
```

> ### Beispiel:
> ```bash
> sudo chown rogerio:users meine_datei.txt
> ```

### chmod
Mit dem Befehl `chmod` kannst du die Berechtigungen einer Datei oder eines Verzeichnisses ändern. Die Berechtigungen können sowohl symbolisch als auch numerisch angegeben werden.
```bash
sudo chmod u+rwx,g+rx,o-r meine_datei.txt
```

Hierbei steht:
- `u`: Besitzer (user)
- `g`: Gruppe (group)
- `o`: Andere (others)
- `+`: Berechtigungen hinzufügen
- `-`: Berechtigungen entfernen


> ### Beispiel:
> ```bash
> sudo chmod 755 meine_datei.txt
> ```
>
> Hierbei hat der Besitzer alle Rechte, und Gruppe und andere haben Lese- und Ausführungsrechte.

### ls -l
Um die aktuellen Berechtigungen einer Datei oder eines Verzeichnisses anzuzeigen, kannst du den Befehl `ls -l` verwenden:
```bash
ls -l
```

Dieser Befehl listet alle Dateien und Verzeichnisse im aktuellen Verzeichnis auf und zeigt deren Berechtigungen an.

---

## Berechnung der Berechtigungen

Die Berechtigungen können auch numerisch mit drei Ziffern (0-7) angegeben werden, wobei jede Ziffer für die Berechtigungen des Besitzers, der Gruppe und anderer Benutzer steht. 

Hier ist, wie die Ziffern funktionieren:
- `4`: Lesen (r)
- `2`: Schreiben (w)
- `1`: Ausführen (x)
- `0`: Keine Berechtigung (-)

Um die numerische Berechtigung zu berechnen, addierst du die Werte für die gewünschten Berechtigungen:

> ### Beispiel 1: 744
> - Besitzer: `rwx` → 4 + 2 + 1 = 7 (Binär: `111`)
> - Gruppe: `r--` → 4 + 0 + 0 = 4 (Binär: `100`)
> - Andere: `r--` → 4 + 0 + 0 = 4 (Binär: `100`)
> - **Ergebnis**: `744` bedeutet, dass der Besitzer alle Rechte hat, die Gruppe und andere Benutzer nur Lesezugriff haben.

> ### Beispiel 2: 654
> - Besitzer: `r-x` → 4 + 0 + 1 = 5 (Binär: `101`)
> - Gruppe: `rw-` → 4 + 2 + 0 = 6 (Binär: `110`)
> - Andere: `--x` → 0 + 0 + 1 = 1 (Binär: `001`)
> - **Ergebnis**: `654` bedeutet, dass der Besitzer Lese- und Ausführungsrechte hat, die Gruppe Lese- und Schreibrechte hat, und andere Benutzer nur Ausführungsrechte haben.


### Binäre Darstellung der Berechtigungen
Jede Berechtigung kann auch als ein Bit dargestellt werden.
- Lesen (r) = 1 (true)
- Schreiben (w) = 1 (true)
- Ausführen (x) = 1 (true)
- Keine Berechtigung = 0 (false)

Die Berechtigungen können in einer binären Zahl dargestellt werden:

| Berechtigung | Binär | Dezimal |
|--------------|-------|---------|
| rwx          | 111   | 7       |
| rw-          | 110   | 6       |
| r-x          | 101   | 5       |
| r--          | 100   | 4       |
| -wx          | 011   | 3       |
| -w-          | 010   | 2       |
| --x          | 001   | 1       |
| ---          | 000   | 0       |


So ergibt die binäre Zahl, die aus den einzelnen Berechtigungen zusammengesetzt ist, die numerische Darstellung der Berechtigungen.
