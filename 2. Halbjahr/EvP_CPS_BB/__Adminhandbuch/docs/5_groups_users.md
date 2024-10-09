# Nutzergruppen und Benutzer hinzufügen 


## Inhaltsverzeichnis
- [Gruppen hinzufügen](#gruppen-hinzufügen)
- [Mittels adduser und passwd](#mittels-adduser-und-passwd)
- [Mittels useradd](#gruppen-anlegen)
- [Nutzer zu Gruppen hinzufügen](#nutzer-zu-gruppen-hinzufügen)

## Gruppen hinzufügen
Verwende den Befehl **groupadd,** um eine Gruppe anzulegen: 
```shell
sudo groupadd GRUPPENNAME 
```
 

## Mittels adduser und passwd
Um einen Nutzer hinzuzufügen, nutze den Befehl **adduser** und **passwd** um einen Benutzer anzulegen: 
```shell
sudo adduser NUTZERNAME 
sudo passwd NUTZERNAME 
```
--- 
Um den Nutzer einer Gruppe hinzuzufügen, verwende den Befehl **usermod**: 
```shell
sudo usermod -aG GRUPPENNAME NUTZERNAME 
```

---
Um alle Gruppen anzeigen, nutze 
```shell
getent group 
```
 

Um alle Gruppen eines Nutzers anzeigen, nutze: 
```shell
groups NUTZERNAME 
```

Wenn du möchtest, dass ein Benutzer sein Passwort beim nächsten Login ändern muss, kannst du den folgenden Befehl verwenden:
```shell
sudo chage -d 0 NUTZERNAME
```