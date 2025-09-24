# Solvabilit-_d-un_client

Loan Approval Prediction
📌 Description

Ce projet consiste à développer un modèle prédictif de validation de prêts basé sur les caractéristiques des demandeurs (revenus, situation familiale, niveau d’éducation, antécédents de crédit, etc.).

L’objectif est de :

Analyser et préparer les données de prêts.

Entraîner un modèle de Machine Learning pour prédire le statut d’approbation d’un prêt (Loan_Status).

Sauvegarder le modèle entraîné pour une utilisation ultérieure.

Préparer une future mise en production via Flask pour fournir une API de prédiction en temps réel.

📂 Dataset

Le dataset utilisé contient les informations suivantes :

Gender : Sexe du demandeur

Married : État matrimonial

Dependents : Nombre de personnes à charge

Education : Niveau d’éducation

Self_Employed : Indique si le demandeur est travailleur indépendant

ApplicantIncome : Revenu principal du demandeur

CoapplicantIncome : Revenu du co-demandeur

LoanAmount : Montant du prêt

Loan_Amount_Term : Durée du prêt (en jours)

Credit_History : Historique de crédit (1 = bon, 0 = mauvais)

Property_Area : Zone géographique (Urbain, Semi-urbain, Rural)

Loan_Status : Statut du prêt (Y = approuvé, N = refusé)

⚙️ Étapes du projet

Exploration et nettoyage des données :

Gestion des valeurs manquantes

Encodage des variables catégorielles

Normalisation des variables numériques

Modélisation :

Séparation des données en train/test

Entraînement de différents modèles (Logistic Regression, Random Forest, etc.)

Sélection du modèle le plus performant

Évaluation :

Précision, recall, F1-score

Matrice de confusion

Sauvegarde du modèle :

Utilisation de Pickle/Joblib pour enregistrer le modèle final

Mise en production (à venir) :

Intégration du modèle dans une API avec Flask

Endpoint permettant de faire des prédictions en temps réel à partir de nouvelles données

🚀 Technologies utilisées

Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)

Flask (prévu pour la mise en production)

📌 Résultats

Un modèle capable de prédire l’approbation des prêts avec une bonne précision.

Un pipeline reproductible, de l’analyse à la sauvegarde du modèle.

Base solide pour déployer une API de scoring de crédit en temps réel.

🔮 Prochaines étapes

Déploiement du modèle avec Flask.

Création d’une interface utilisateur simple pour la saisie des données et la prédiction.

Intégration possible avec un tableau de bord interactif.
