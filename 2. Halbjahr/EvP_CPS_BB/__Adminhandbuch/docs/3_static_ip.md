# Einrichten einer statischen IP-Adresse mit nmtui

Öffne ein Terminal und gebe den folgenden Befehl ein, um das **NetworkManager Text User Interface (nmtui)** zu starten:
```shell
nmtui
```

Wähle die Option **"Edit a connection"** aus und Wähle die Verbindung aus, die du bearbeiten möchtest (z. B. Ethernet oder Wi-Fi), und drücke **Enter**.

Navigiere zu **"IPv4 CONFIGURATION"**.

Setze die Konfiguration auf **"Manual"**.

Füge die statische IP-Adresse, die Subnetzmaske und das Gateway ein:
> - **Adresse**: (z. B. 192.168.1.100)
> - **Subnetzmaske**: (z. B. 255.255.255.0)
> - **Gateway**: (z. B. 192.168.1.1)

Füge die DNS-Server hinzu (z. B. 8.8.8.8 für Google DNS).

Navigiere zu **"OK"** und drücke **Enter**, um die Änderungen zu speichern.

Gehe zurück zum Hauptmenü und wähle **"Activate a connection"**.
Wähle die bearbeitete Verbindung aus und aktiviere sie.

Um zu überprüfen, ob die statische IP-Adresse erfolgreich eingerichtet wurde, kannst du den folgenden Befehl verwenden:
```shell
ip addr show
```

Du solltest jetzt eine statische IP-Adresse für deine Verbindung konfiguriert haben.
