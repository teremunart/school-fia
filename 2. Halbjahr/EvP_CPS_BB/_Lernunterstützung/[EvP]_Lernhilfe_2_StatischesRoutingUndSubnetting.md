Themen für die Klausur am 9.04.2025 

IPv4
- Private, öffentliche IP-Adressbereiche der Klassen A, B, C
- Local loop (127.0.0.1)

Subnetting mit IPv4
- Warum, Vorteile, Nachteile
- Umwandeln eines Oktetts in eine Bitfolge und umgekehrt
- Aufbau (Netzanteil, Subnetzanteil, Hostanteil)
- Subnetzmaske (SM) und dessen Bedeutung und Schreibweisen (binär, CIDR=/, dez. Punktnotation)
- Netzadresse, Hostadressen, Broadcastadresse
- Subnetze bilden 
 - Maximal viele: wie viele Subnetze? Neue SM?, Anzahl Hostadressen pro Subnetz? 
 - bestimmte Anzahl: Neue SM?, Anzahl Hostadressen pro Subnetz?,  1. (mit Nr. 0) , 2. .. letzte Netzadresse? 

IPv6
- Warum, Vorteile, Nachteile
- Umwandeln eines Hextets in eine Bitfolge und umgekehrt
- Aufbau (Netz-Prefix, Global Routing Prefix, Prefixlänge, Netz-ID-Anteil)
- Verkürzen, verlängern
- Arten von IPv6-Adressen (GUA, LLA, Multicast), Beispiele
- Scope (lokal im Subnetz, lokal im LAN, weltweit)
- Subnetze bilden
 - Maximal viele: wie viele? Neue Prefixlänge?
 - bestimmte Anzahl: Neue Prefixlänge?,  1., 2. .. Netzadresse? Keine Broadcastadressen vorhanden 

statisches Routing
- Notwendige Teile der Netzwerkkonfiguration eines Clients (PC, Laptop), für die Kommunikation im Netzwerk/Internet
- Standard-Gateway und dessen Bedeutung/Aufgabe
- Netzwerktopologie mit Subnetzen, Switch, Router, Internet zeichnen
- Aufbau einer Routingtabelle (Spaltenüberschriften und deren Bedeutung, Zeilen und deren Funktionsweise für den Routingprozess)
- Routingtabellen: Zeileneinträge: Route zu angrenzenden Subnetzen, Default Route, Routen zu nicht angrenzenden Subnetzen
- PC schickt ein Beispielpaket über Router bis zum Ziel und zurück: Vorgang Schritt für Schritt beschreiben
- Fehler in Routingtabelle finden  

Transport eines Pakets im LAN-Netzwerk
- Bedeutung einer MAC-Adresse im Subnetz (L2)
- Bedeutung der IP-Adresse als End-zu-End-Adresse (L3)
- End-zu-End-Transport eines Pakets über IP- und MAC-Adressen 

Finden der MAC-Adresse zur Ziel-IP-Adresse (next Hop: PC, Standard-Gateway, Router) 
- Kapselung L2 (Frame), L3 (IP-Paket) 
- Transport vom PC zum Standard-Gateway 
- Transport vom Router zu Router 
- Transport vom Router zum Ziel-PC 