# Projet Python - Gestion de Boutique avec MySQL


---

## Objectif du programme

Le programme permet de gérer les produits d’une boutique :

-  Ajouter un produit
-  Afficher la liste des produits
-  Modifier la quantité d’un produit
-  Rechercher un produit
-  Supprimer un produit
-  Afficher des statistiques (dashboard)

Technologies utilisées :

- Python 
- MySQL 
- Module `mysql.connector`

---

## Structure générale du programme

Le programme est composé de :

1. Connexion à la base de données MySQL
2. Fonctions pour gérer les produits
3. Un menu interactif
4. Une boucle principale (`main`) qui exécute le programme

---

## Connexion à la base de données

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Boutique_du_quartier"
)

curseur = conn.cursor()
