# Lernhilfe 2 Datenbanken & SQL

## Begriffe abgrenzen

|          | Begriff                              | Bedeutung                                                           |
|----------|--------------------------------------|---------------------------------------------------------------------|
| **DBS**  | (Datenbank-System)                   | DB + DBMS → komplettes System                                       |
| **DBMS** | (Datenbank-Managementsystem)         | Software zur Verwaltung der Datenbank                               |
| **DB**   | (Datenbank)                          | Strukturierte Sammlung von Daten                                    |
| **DD**   | (Datenbank-Design / Data Dictionary) | Beschreibung der Datenstruktur (z.B. Tabellen, Spalten, Datentypen) |
| **DDL**  | (Data Definition Language)           | Sprache zur Definition der Datenstruktur (z.B. CREATE, ALTER, DROP) |
| **DML**  | (Data Manipulation Language)         | Sprache zur Manipulation von Daten (z.B. SELECT, INSERT, UPDATE)    |
| **DCL**  | (Data Control Language)              | Sprache zur Kontrolle der Zugriffsrechte (z.B. GRANT, REVOKE)       |

| Begriff                  | Bedeutung                                                                      |
|--------------------------|--------------------------------------------------------------------------------|
| **ER-Modell**            | (Entity-Relationship-Modell) – Beschreibung der Daten und ihrer Beziehungen    |
| **Primärschlüssel (PK)** | Eindeutiges Attribut oder Attributkombination zur Identifikation einer Zeile   |
| **Fremdschlüssel (FK)**  | Attribut, das auf den Primärschlüssel einer anderen Tabelle verweist           |
| **Normalisierung**       | Prozess zur Vermeidung von Redundanz und Verbesserung der Datenintegrität      |
| **Denormalisieren**      | Bewusste Aufhebung der Normalisierung für bessere Performance                  |
| **Index**                | Datenstruktur zur Beschleunigung von Abfragen                                  |
| **Transaktion**          | Eine Gruppe von SQL-Befehlen, die als atomare Einheit ausgeführt wird          |
| **ACID**                 | Eigenschaften einer Transaktion: Atomicity, Consistency, Isolation, Durability |
| **View (Sicht)**         | Virtuelle Tabelle, basierend auf einer SELECT-Abfrage                          |
| **Stored Procedure**     | Vorgefertigtes SQL-Programm, das auf dem Server ausgeführt wird                |
| **Trigger**              | Automatisch ausgeführte Aktion bei bestimmten Ereignissen (z.B. INSERT)        |
| **Schema**               | Logische Struktur einer Datenbank (enthält Tabellen, Views etc.)               |
| **Constraint**           | Bedingung für die Datenintegrität (z. B. NOT NULL, UNIQUE, CHECK)              |
| **JOIN**                 | SQL-Operation zum Kombinieren von Daten aus mehreren Tabellen                  |



---

## Eigenschaften eines DBMS

- Ein DBMS trennt die Speicherung der Daten von der Anwendung, wodurch Änderungen an der Datenstruktur keine Anpassung im Programmcode erfordern.
- Es stellt sicher, dass nur gültige und konsistente Daten gespeichert werden, indem Regeln wie Primärschlüssel oder Prüfbedingungen verwendet werden.
- Es erlaubt mehreren Benutzern gleichzeitig auf die Daten zuzugreifen, ohne dass es zu Konflikten oder Datenverlust kommt.
- Transaktionen werden zuverlässig abgewickelt, wobei das ACID-Prinzip (Atomarität, Konsistenz, Isolation, Dauerhaftigkeit) eingehalten wird.
- Das System schützt die Daten vor unberechtigtem Zugriff durch ein ausgefeiltes Rechte- und Rollenkonzept.
- Es verhindert, dass dieselben Informationen mehrfach gespeichert werden, indem es Daten zentral organisiert und Beziehungen nutzt.
- Ein DBMS sorgt dafür, dass die Daten auch nach Fehlern oder Systemausfällen in einem korrekten und konsistenten Zustand bleiben.

---

## SQL Grundlagen

### JOINS

#### `INNER JOIN`
Nur gemeinsame Datensätze in beiden Tabellen

```sql
SELECT * 
FROM Kunden
INNER JOIN Bestellungen ON Kunden.ID = Bestellungen.KundenID;
```

#### `LEFT OUTER JOIN`
Alle Kunden, auch ohne Bestellung

```sql
SELECT * 
FROM Kunden
LEFT JOIN Bestellungen ON Kunden.ID = Bestellungen.KundenID;
```


#### `RIGHT OUTER JOIN`
Alle Bestellungen, auch ohne passenden Kunden. Nicht von SQLite unterstützt.

```sql
SELECT * 
FROM Kunden
RIGHT JOIN Bestellungen ON Kunden.ID = Bestellungen.KundenID;
```

---

| JOIN-Typ          | Ergebnis                                                            |
|-------------------|---------------------------------------------------------------------|
| `INNER JOIN`      | Nur die **gemeinsamen** Datensätze                                  |
| `LEFT JOIN`       | Alles aus **links**, plus passende aus rechts                       |
| `RIGHT JOIN`      | Alles aus **rechts**, plus passende aus links                       |
| `FULL OUTER JOIN` | Alles aus beiden Tabellen (Überschneidung und Nicht-Überschneidung) |


---

### Subselect (Unterabfrage)

```sql
SELECT Name 
FROM Kunden 
WHERE ID IN (
  SELECT KundenID 
  FROM Bestellungen 
  WHERE Betrag > 100
);
```

---

### Aggregatfunktionen

| Funktion      | Beschreibung   |
|---------------|----------------|
| `COUNT(*)`    | Zählt Zeilen   |
| `SUM(Betrag)` | Summiert Werte |
| `AVG(Betrag)` | Durchschnitt   |
| `MIN(Betrag)` | Kleinster Wert |
| `MAX(Betrag)` | Größter Wert   |

```sql
SELECT AVG(Betrag) AS Durchschnitt
FROM Bestellungen
WHERE KundenID = 1;
```

---

**Merktipp**:
- **JOINs** → "Was will ich verbinden?"
- **Subselect** → "Ich frage etwas, das sich auf ein anderes Ergebnis bezieht."
- **DBMS vs. DB** → "DBMS ist der Verwalter, DB ist der Inhalt."

