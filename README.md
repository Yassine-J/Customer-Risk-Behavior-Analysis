# 📊 Analyse du churn client – secteur bancaire

## 🎯 Objectif du projet
Ce projet vise à analyser le comportement de 10 000 clients bancaires afin d’identifier les principaux facteurs de churn (départ des clients) et de proposer des recommandations concrètes pour améliorer la rétention.

---

## 📁 Données
- Dataset : Bank Customer Churn Prediction sur Kaggle
- Taille : 10 000 clients
- Variables : âge, pays, solde, nombre de produits, activité, etc.

---

## 🧠 Problématique métier
Le churn représente une perte importante pour les banques, car il est plus coûteux d’acquérir un nouveau client que de fidéliser un client existant.

👉 Objectif : identifier les profils à risque et comprendre les facteurs qui expliquent le départ des clients.

---

## 🔍 Méthodologie
- Nettoyage et préparation des données
- Analyse exploratoire (EDA)
- Analyse du churn global
- Analyse par variables (âge, pays, activité, produits…)
- Segmentation simple des clients
- Création d’indicateurs business
- Visualisation des résultats
- Export des données pour dashboard Power BI

---

## 📊 Résultats clés

- 📉 Taux de churn global : **20,37%** (≈ 1 client sur 5)

- 👥 Les clients qui churnent sont en moyenne plus âgés  
  → 44,8 ans vs 37,4 ans

- ⚡ Les clients inactifs ont un taux de churn presque 2 fois plus élevé  
  → 26,85% vs 14,27%

- 🌍 L’Allemagne présente le churn le plus élevé  
  → 32,44% (vs ~16% en France et Espagne)

- 🏦 Les clients avec 2 produits sont les plus fidèles  
  → 7,58% de churn vs 27,7% pour 1 produit

- ⚠️ Les segments avec 3 et 4 produits présentent un churn élevé  
  mais leurs effectifs sont faibles → interprétation prudente

---

## 💡 Recommandations business

- Mettre en place des campagnes de réactivation pour les clients inactifs
- Encourager le multi-équipement (cross-sell)
- Analyser le marché allemand pour comprendre les causes du churn élevé
- Cibler les clients à forte valeur (solde élevé) avec des offres adaptées

---

## 🛠️ Technologies utilisées
- Python (pandas, matplotlib)
- Power BI (dashboard interactif)
- GitHub

---

## 📈 Visualisations
Les principales visualisations incluent :
- Répartition du churn
- Churn par pays
- Churn par activité
- Churn par nombre de produits

---

## 📂 Structure du projet

```text
.
├── data/
│   └── Bank Customer Churn Prediction.csv
├── images/
│   ├── churn_global.png
│   ├── churn_par_activite.png
│   ├── churn_par_pays.png
│   ├── churn_par_produits.png
│   └── dashboard_pbi_churn.png
├── bank_churn_cleaned.csv
├── CRB.py
└── README.md
```
---

## 🚀 Perspectives d’amélioration
- Modélisation prédictive du churn (Machine Learning)
- Segmentation avancée des clients
- Analyse temporelle du churn
- Déploiement d’un dashboard interactif avancé

---

## 👤 Auteur
Étudiant en L3 Informatique – Université de Montpellier  
Spécialisation : Data / Business Intelligence / Analyse de données

---

## ⭐ Objectif du projet
Ce projet s’inscrit dans une démarche de développement de compétences en data analysis et de préparation à une alternance en Data Analyst / Business Intelligence.
