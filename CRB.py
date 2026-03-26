# ============================================================
# PROJET : Analyse du churn client (secteur bancaire)
# OBJECTIF :
# Analyser les comportements clients pour identifier les profils
# à risque et aider à la prise de décision.
# ============================================================

# ---------------------------
# 1. IMPORT DES LIBRAIRIES
# ---------------------------
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 2. CHARGEMENT DU DATASET
# ---------------------------
df = pd.read_csv("Bank Customer Churn Prediction.csv")

print("Aperçu du dataset :")
print(df.head())

print("\nColonnes :")
print(df.columns.tolist())

print("\nDimensions (lignes, colonnes) :")
print(df.shape)

# ---------------------------
# 3. VÉRIFICATION DES DONNÉES
# ---------------------------
print("\nInformations générales :")
df.info()

print("\nValeurs manquantes :")
print(df.isna().sum())

# ---------------------------
# 4. NETTOYAGE DES DONNÉES
# ---------------------------
# Suppression de l'identifiant client (inutile pour l'analyse)
cols_to_drop = ["customer_id"]
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

print("\nColonnes après nettoyage :")
print(df.columns.tolist())

# ---------------------------
# 5. ANALYSE DU CHURN GLOBAL
# ---------------------------
print("\nRépartition des clients :")
print(df["churn"].value_counts())

taux_churn = df["churn"].mean() * 100
print(f"\nTaux de churn global : {taux_churn:.2f}%")

# ---------------------------
# 6. ANALYSE PAR VARIABLES
# ---------------------------

# 6.1 Analyse de l'âge
print("\nÂge moyen selon churn :")
print(df.groupby("churn")["age"].mean())

# 6.2 Analyse de l'activité client
print("\nChurn selon activité :")
print(pd.crosstab(df["active_member"], df["churn"], normalize="index") * 100)

# 6.3 Analyse du nombre de produits
print("\nChurn selon nombre de produits :")
print(pd.crosstab(df["products_number"], df["churn"], normalize="index") * 100)

print("\nEffectifs par nombre de produits :")
print(df["products_number"].value_counts().sort_index())

# 6.4 Analyse par pays
print("\nChurn par pays :")
print(pd.crosstab(df["country"], df["churn"], normalize="index") * 100)

# 6.5 Analyse du solde
print("\nSolde moyen selon churn :")
print(df.groupby("churn")["balance"].mean())

# 6.6 Analyse du genre
print("\nChurn selon genre :")
print(pd.crosstab(df["gender"], df["churn"], normalize="index") * 100)

# ---------------------------
# 7. SEGMENTATION CLIENT (SIMPLE)
# ---------------------------
balance_median = df["balance"].median()

def segment_client(row):
    if row["churn"] == 1:
        return "À risque"
    elif row["active_member"] == 1 and row["balance"] > balance_median:
        return "Client fidèle premium"
    else:
        return "Client standard"

df["segment"] = df.apply(segment_client, axis=1)

print("\nRépartition des segments :")
print(df["segment"].value_counts())

# ---------------------------
# 8. INSIGHTS AUTOMATIQUES
# ---------------------------
print("\n========== INSIGHTS ==========\n")

# Insight 1
print(f"Taux global de churn : {taux_churn:.2f}%")

# Insight 2 : âge
age_stay = df[df["churn"] == 0]["age"].mean()
age_leave = df[df["churn"] == 1]["age"].mean()
print(
    f"Les clients qui partent sont en moyenne plus âgés "
    f"({age_leave:.1f} ans) que ceux qui restent ({age_stay:.1f} ans)."
)

# Insight 3 : activité
churn_actif = df[df["active_member"] == 1]["churn"].mean() * 100
churn_inactif = df[df["active_member"] == 0]["churn"].mean() * 100
print(
    f"Les clients inactifs présentent un taux de churn plus élevé "
    f"({churn_inactif:.2f}%) que les clients actifs ({churn_actif:.2f}%)."
)

# Insight 4 : pays
churn_pays = df.groupby("country")["churn"].mean().sort_values(ascending=False) * 100
print(
    f"Le pays avec le churn le plus élevé est {churn_pays.index[0]} "
    f"({churn_pays.iloc[0]:.2f}%)."
)

# Insight 5 : produits
churn_produits = df.groupby("products_number")["churn"].mean().sort_values(ascending=False) * 100
print(
    f"Le segment produits le plus à risque est celui avec {churn_produits.index[0]} produit(s) "
    f"({churn_produits.iloc[0]:.2f}% de churn)."
)


print("\n=============================\n")

# ---------------------------
# 9. VISUALISATIONS
# ---------------------------

# 1. Churn global
df["churn"].value_counts().plot(kind="bar")
plt.title("Répartition du churn")
plt.xlabel("Churn")
plt.ylabel("Nombre de clients")
plt.tight_layout()
plt.savefig("churn_global.png")
plt.show()

# 2. Churn par pays
(df.groupby("country")["churn"].mean() * 100).sort_values(ascending=False).plot(kind="bar")
plt.title("Taux de churn par pays")
plt.xlabel("Pays")
plt.ylabel("Taux de churn (%)")
plt.tight_layout()
plt.savefig("churn_par_pays.png")
plt.show()

# 3. Churn par activité
(df.groupby("active_member")["churn"].mean() * 100).plot(kind="bar")
plt.title("Taux de churn selon l'activité")
plt.xlabel("Actif (0 = non, 1 = oui)")
plt.ylabel("Taux de churn (%)")
plt.tight_layout()
plt.savefig("churn_par_activite.png")
plt.show()

# 4. Churn par produits
(df.groupby("products_number")["churn"].mean() * 100).plot(kind="bar")
plt.title("Taux de churn par nombre de produits")
plt.xlabel("Nombre de produits")
plt.ylabel("Taux de churn (%)")
plt.tight_layout()
plt.savefig("churn_par_produits.png")
plt.show()

# ---------------------------
# 10. EXPORT POUR POWER BI
# ---------------------------
df.to_csv("bank_churn_cleaned.csv", index=False)
print("\nEffectifs par nombre de produits :")
print(df["products_number"].value_counts().sort_index())
print("Fichier exporté : bank_churn_cleaned.csv")