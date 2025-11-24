# 💳 Solvabilité d’un client – Prédiction d’Approbation de Prêt

## 📝 Description

Ce projet vise à développer un modèle prédictif pour évaluer la **solvabilité d’un client** et prédire l’approbation d’un prêt en fonction de ses caractéristiques personnelles et financières (revenus, situation familiale, niveau d’éducation, antécédents de crédit, etc.).

**Objectifs :**

- Explorer et préparer les données de prêts.  
- Entraîner et comparer différents modèles de Machine Learning.  
- Identifier le modèle le plus performant selon la **métrique prioritaire : Recall**, afin de détecter un maximum de clients risqués.  
- Sauvegarder le modèle pour une utilisation ultérieure.  
- Préparer une future mise en production via une API Flask pour des prédictions en temps réel.

---

## 📊 Dataset

Le dataset contient les informations suivantes :

- **Gender** : Sexe du demandeur  
- **Married** : État matrimonial  
- **Dependents** : Nombre de personnes à charge  
- **Education** : Niveau d’éducation  
- **Self_Employed** : Travailleur indépendant  
- **ApplicantIncome** : Revenu principal  
- **CoapplicantIncome** : Revenu du co-demandeur  
- **LoanAmount** : Montant du prêt  
- **Loan_Amount_Term** : Durée du prêt (en jours)  
- **Credit_History** : Historique de crédit (1 = bon, 0 = mauvais)  
- **Property_Area** : Zone géographique (Urbain, Semi-urbain, Rural)  
- **Loan_Status** : Statut du prêt (1 = approuvé, 0 = refusé)  

---

## ⚙️ Étapes du projet

### 1️⃣ Exploration et prétraitement des données

- Analyse des valeurs manquantes  
- Encodage des variables catégorielles  
- Normalisation des variables numériques  

### 2️⃣ Modélisation

- Séparation des données en train/test  
- Entraînement et comparaison de plusieurs modèles de Machine Learning  
- Sélection du meilleur modèle selon la **métrique prioritaire : Recall**, pour détecter un maximum de mauvais payeurs et réduire le risque de défaut  

### 3️⃣ Évaluation

- Matrice de confusion  
- Métriques : Accuracy, Recall, F1-score, ROC-AUC  
- Analyse métier pour identifier le modèle le plus adapté au scoring crédit  

### 4️⃣ Sauvegarde du modèle

- Le modèle final est enregistré pour une utilisation future et pour une mise en production  

### 5️⃣ Mise en production (prévue)

- Déploiement du modèle via Streamlit 
- API pour prédiction en temps réel à partir de nouvelles données  
- Intégration possible avec un tableau de bord interactif  

---

## 🏆 Résultats

- Le modèle choisi est **  En cours **, qui présente un **Recall élevé **, permettant de détecter presque tous les mauvais payeurs.  
- Ce choix minimise le **risque de défaut**, prioritaire dans un contexte bancaire.  
- Le pipeline est reproductible, de l’analyse à la sauvegarde du modèle.  

---

## 🛠️ Technologies utilisées

- **Python** : Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Streamlit** (prévu pour la mise en production)  

---

## 🔮 Prochaines étapes

- Déploiement du modèle avec Streamlit
- Création d’une interface utilisateur simple pour saisir les données et obtenir la prédiction  
- Intégration possible avec un tableau de bord interactif pour le suivi du scoring  
