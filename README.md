# API de scoring client
## Objectif 
Création d'une api permettant de réaliser des prédictions vis à vis de l'octroi d'un prêt selon des données client récolté en amont.
## Description des éléments
### .GitHub/workflows
Dossier contenant le code permettant le déploiement automatique de l'api et la réalisation des différents tests unitaire (deploy_v2.yml).
### api
Dossier déployé à l'aide de deploy_v2. Il contient l'ensemble des éléments nécessaires à l'exécution de l'api :
- api_test_pe.csv : les données des différents clients.
- app_api.py : le fichier contenant le code de l'api.
- model_lgbm.pkl : le modèle entraîné qui sera utiliser pour les prédictions.
- requirements.txt : les différentes librairies nécessaires à l'utilisation.
### Modelisation.ipynb
Le notebook contenant le code ayant servi à traiter les fichiers clients en amont ([lien vers les fichiers](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Impl%C3%A9menter+un+mod%C3%A8le+de+scoring/Projet+Mise+en+prod+-+home-credit-default-risk.zip)).
Il utilise les deux kernels kaggle suivant :
- [analyse exploratoire](https://www.kaggle.com/code/willkoehrsen/start-here-a-gentle-introduction/notebook)
- [préparation des données](https://www.kaggle.com/code/jsaguiar/lightgbm-with-simple-features/script)
Il contient également le code ayant servi à tester les différents modèles.
### Test.api.py
Fichier contenant le code permettant d'effectuer les tests unitaires pour vérifier le bon fonctionnement de l'api.
## Utilisation de l'api
Pour utiliser l'api il suffit d'utiliser une URL construite de la façon suivante :
url+id_client
- l'url de base d'appel du modèle est : https://6equal.pythonanywhere.com/predict/
- l'id client est un nombre entier (par exemple : 400958)