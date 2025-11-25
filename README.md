# 💳 Solvabilité d’un client – Prédiction d’Approbation de Prêt

**Développé par : DJAKAS Yawo Justin**  
- LinkedIn : [https://www.linkedin.com/in/yawo-justin-djakas/](https://www.linkedin.com/in/yawo-justin-djakas/)  
- GitHub : [https://github.com/Just1919](https://github.com/Just1919)  

**Lien de l'App Streamlit :** [https://solvabilit-d-unclient-uvgubixdmwnqn7qhrxlgvb.streamlit.app/](https://solvabilit-d-unclient-uvgubixdmwnqn7qhrxlgvb.streamlit.app/)

---

## 📝 Description

Ce projet vise à développer un modèle prédictif pour évaluer la **solvabilité d’un client** et prédire l’approbation d’un prêt en fonction de ses caractéristiques personnelles et financières (revenus, situation familiale, niveau d’éducation, antécédents de crédit, etc.).

**Objectifs :**

- Explorer et préparer les données de prêts  
- Entraîner et comparer différents modèles de Machine Learning  
- Identifier le modèle le plus performant selon la **métrique prioritaire : Recall**, afin de détecter un maximum de clients risqués  
- Sauvegarder le modèle pour une utilisation ultérieure  
- Préparer la mise en production via Streamlit et API pour des prédictions en temps réel

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
- Entraînement et optimisation d’un pipeline **LogisticRegression_L2** avec GridSearchCV  
- Sélection du meilleur modèle selon le **Recall**, pour détecter un maximum de mauvais payeurs  

### 3️⃣ Évaluation

**Résultats sur le jeu test :**
=== LogisticRegression_L2 optimisée ===
Meilleur C : 0.1, Seuil optimisé : 0.50

Classification report :
  precision recall     f1-score support
0 0.72     0.68        0.70      38
1 0.86    0.88         0.87     85
accuracy               0.82       123


- Analyse métier pour identifier le modèle le plus adapté au scoring crédit  

### 4️⃣ Sauvegarde du modèle

- Le modèle final est enregistré dans `model/` pour une utilisation future et pour la mise en production  

### 5️⃣ Mise en production (prévue)

- Déploiement via **Streamlit**  
- API pour prédiction en temps réel  
- Intégration possible avec un tableau de bord interactif  

---

## 🛠️ Technologies utilisées

- **Python** : Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Streamlit** pour la mise en production  



