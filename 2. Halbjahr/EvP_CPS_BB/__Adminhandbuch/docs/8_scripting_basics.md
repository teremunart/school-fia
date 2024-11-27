# Scripting Grundlegende Information

---

## Inhaltsverzeichnis
- [Kurzerklärung](#kurzerklärung)
- [Shebang #!](#shebang)
- [Variablen](#variablen)
- [Kontrollstrukturen](#kontrollstrukturen)
  - [Bedingte Anweisungen](#bedingte-anweisungen)
  - [Schleifen](#schleifen)
- [Kommentare](#kommentare)
- [Dateiberechtigung](#dateiberechtigungen)

---

## Kurzerklärung

Scripting ist die Erstellung von automatisierten Prozessen mithilfe von 
Skriptsprachen. Skripte werden häufig zur Automatisierung von 
Routineaufgaben, für Systemadministration, Datenverarbeitung oder zur 
schnellen Entwicklung von Anwendungen verwendet. 


Skriptsprachen sind in der Regel interpretierte Sprachen, d.h. sie werden 
von einem Interpreter zur Laufzeit ausgeführt und nicht vorab kompiliert. 
<br><br>Zu den bekanntesten Skriptsprachen gehören:

- **Bash** (Unix/Linux Shell-Skripting)
- **Python** (universelle Skriptsprache)
- **JavaScript** (Webentwicklung)
- **PowerShell** (Windows-Administration)

---

## Shebang (#!)

Der Shebang ist die erste Zeile eines Skripts und gibt an, welcher 
Interpreter das Skript ausführen soll. Er beginnt mit `#!` gefolgt vom 
Pfad des Interpreters.

```bash
#!/bin/bash
# Dies ist ein Bash-Skript
echo "Hallo Welt!"
```

Für Python: `#!/usr/bin/python3`

---

## Variablen

In Skripten sind Variablen Speicherorte für Daten. Die Syntax variiert je 
nach Sprache.

```bash
# Bash:
NAME="Rogerio"
echo "Hallo, $NAME!"
```

```python
# Python:
name = "Rogerio"
print(f"Hallo, {name}!")
```

---

## Kontrollstrukturen

Kontrollstrukturen sind wichtig, um den Programmfluss zu steuern. 
Dazu gehören Bedingungen, Schleifen und Funktionen.

### Bedingte Anweisungen

```bash
# Bash: if-Bedingung
if [ $NAME == "Jan" ]; then
  echo "Willkommen, Jan!"
else
  echo "Unbekannter Benutzer"
fi
# fi = end
```

```python
# Python: if-Bedingung
if name == "Benjamin":
    print("Willkommen, Benjamin!")
else:
    print("Unbekannter Benutzer")
```

### Schleifen

```bash
# Bash: for-Schleife
for i in {1..5}; do
  echo "Durchlauf $i"
done
```

```python
# Python: for-Schleife
for i in range(1, 6):
    print(f"Durchlauf {i}")
```

---

## Kommentare

Kommentare dienen zur Dokumentation des Codes und werden vom Interpreter 
ignoriert.

```bash
# Dies ist ein einzeiliger Kommentar in Bash
```

```python
# Dies ist ein einzeiliger Kommentar in Python
```

---

## Dateiberechtigungen

Um ein Skript auszuführen wird der Befehl `chmod` genutzt:

```bash
chmod +x mein_skript.sh
./mein_skript.sh
```
Um skript ohne angabe von z.B. bash auszuführen muss shebang gesetzt sein
Mit angabe von bash kann auch ohne Ausführungsrechte ausgeführt werden
