# Objectifs 

Dans le cadre d'un projet domotique lié à une pièce de théâtre réalisé par une classe de première ES, nous avons été convoqué 
afin de concevoir un pupitre accompagné de plusieurs leds qui s'allument et s'éteignent de façon aléatoire et jouer une musique 
de fond. 

Ce pupitre sera joint à d'autres projets tel qu'un ascenseur ou une application 
mobile capable d'orchestrer le pupitre et l'ascenseur.

# Dépendances 

## pypitre

### Depuis pypi.org
* pyserial 
* RPi.GPIO 
* omxplayer-wrapper

```bash
sudo pip3 install pyserial RPi.GPIO omxplayer-wrapper 
```

### Sur le Raspberry PI cible 
* Python >= 3.5
* omxplayer

```bash
sudo apt update; sudo apt upgrade 
sudo apt install omxplayer python3
```
# Installation 

```bash 
git clone https://github.com/Reachip/projet-theatre
sudo python3 projet-theatre/pypitre
```

Utillisez le fichier ```config.json``` afin d'indiquer au programme les trois PIN GPIO qui serviront à allumer les lumières et ou trouver le fichier qui jouera la musique.


