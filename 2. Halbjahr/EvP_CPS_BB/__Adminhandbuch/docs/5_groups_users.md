# Nutzergruppen und Benutzer hinzufügen 

Verwende den Befehl **groupadd** um eine Gruppe anzulegen: 
```shell
sudo groupadd GRUPPENNAME 
```
 

und anschließend den Befehl **adduser** und  passwd um einen Benutzer anzulegen: 
```shell
sudo adduser NUTZERNAME 
sudo passwd NUTZERNAME 
```
 
Um den Nutzer einer Gruppe hinzuzufügen, verwende den Befehl **usermod**: 
```shell
sudo usermod -aG GRUPPENNAME NUTZERNAME 
```
 

Um alle Gruppen anzeigen, nutze 
```shell
getent group 
```
 

Um alle Gruppen eines Nutzers anzeigen, nutze: 
```shell
groups NUTZERNAME 
```