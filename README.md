# freesenegal

# Script de Retweet Automatique avec Message Personnalisé

Ce script utilise l'API Twitter et la bibliothèque Tweepy pour retweeter automatiquement un tweet avec un message personnalisé à intervalles réguliers.

## Configuration requise
- Python 3.x
- Bibliothèque Tweepy : `pip install tweepy`

## Instructions
1. Assurez-vous d'avoir les clés d'authentification de l'API Twitter nécessaires.
2. Remplacez les valeurs `"YOUR_CONSUMER_KEY"`, `"YOUR_CONSUMER_SECRET"`, `"YOUR_ACCESS_TOKEN"`, `"YOUR_ACCESS_TOKEN_SECRET"` par vos propres clés d'authentification dans le script.
3. Remplacez `"YOUR_TWEET_ID"` par l'ID du tweet que vous souhaitez retweeter.
4. Exécutez le script en utilisant la commande `python script.py`.

## Fonctionnement
1. Le script établit une connexion à l'API Twitter en utilisant les clés d'authentification fournies.
2. À l'aide de la fonction `update_status()` de Tweepy, le script retweete le tweet spécifié avec un message personnalisé.
3. Après chaque retweet, le script attend une minute en utilisant `time.sleep10)` avant de retweeter le tweet suivant.
4. Le processus se répète en boucle jusqu'à ce que le script soit arrêté.

## Auteur
MosikasikaC19
