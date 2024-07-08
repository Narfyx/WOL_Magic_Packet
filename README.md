# WOL_Magic_Packet

Ce projet contient un script Python simple pour envoyer un Magic Packet et réveiller un ordinateur à distance via le protocole Wake On LAN (WOL).

## Introduction

Wake On LAN (WOL) est un protocole qui permet de réveiller un ordinateur en veille ou éteint via un réseau local (LAN) en envoyant un paquet réseau spécial appelé "Magic Packet".

## Fonctionnement de Wake On LAN

Le Magic Packet est une trame de données spécifiquement conçue pour le WOL. Il contient la séquence suivante :

1. **Préambule** : Une série de 6 octets avec la valeur 0xFF.
2. **Adresse MAC** : L'adresse MAC de la carte réseau de l'ordinateur cible répétée 16 fois de suite.

Lorsqu'un ordinateur reçoit un Magic Packet avec sa propre adresse MAC, la carte réseau envoie un signal pour réveiller l'ordinateur.

## Configuration nécessaire

Pour que WOL fonctionne, les conditions suivantes doivent être remplies :

1. **Carte réseau (NIC)** : L'ordinateur doit avoir une carte réseau compatible avec WOL.
2. **BIOS/UEFI** : Le support WOL doit être activé dans le BIOS ou l'UEFI de l'ordinateur.
3. **Système d'exploitation** : Le système d'exploitation doit être configuré pour permettre à la carte réseau de réagir aux Magic Packets.
