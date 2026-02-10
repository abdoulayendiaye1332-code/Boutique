import mysql.connector

#connexion a la base de données

conn = mysql.connector.connect(

    host = "localhost",                    #  ========  Adresse du serveur MySQL =======
    user ="root",                            # ========= Nom d'utilisateur MySQL =========
    password = "",                   # ========== Mot de passe MySQL===============
    database= "Boutique_du_quartier"            # ==========  Nom de la base de données==================
)

curseur = conn.cursor()         # Création du curseur pour exécuter les requêtes SQL

#===============================LA FONCTION POUR AJOUTER DES PRODUITS ===============================#

def Ajouter_produit ():

    # Demander les informations du produit à l'utilisateur
    
    nom = input("entrer le nom : ")

    categorie= input ("categorie: ")

    prix = float(input("montant: "))        # conversion en nombre décimal

    quantite = int(input("quantite: "))         # conversion en nombre entier

    # Requête SQL pour insérer un produit dans la table produits

    sql ="insert into produits (nom , categorie , prix ,quantite) values (%s, %s, %s, %s)" 

  # Exécution de la requête avec les valeurs saisies

    curseur.execute (sql,(nom , categorie , prix ,quantite))

    # Validation de l'insertion dans la base de données

    conn.commit()

    print("produit ajouté")

    #===========================================LA FONCTION POUR LISTER LES INVENTAIRES DES PRODUITS=====================================


def liste_inventaire ():

         

    curseur.execute("select * from produits")

    produits = curseur.fetchall()

    print("inventaire")

    for p in produits:

        print(f"id: {p[0]} | nom: {p[1]} | Catégorie: {p[2]} | Prix: {p[3]} | Quantité: {p[4]}")

#==================================================LA FONCTION POUR METTRE A JOUR LES LES PRODUITS =========================================

def Mettre_a_jour():

    id_prod = int(input("id du produit: "))

    nouvelle_quantite = int (input("nouvelle quantite: "))
    
    sql = "update produits set quantite = %s where id = %s"

    curseur.execute(sql,(nouvelle_quantite, id_prod))

    conn.commit()

    print("quantite mise a jour")

#====================================================LA FONCTION POUR RECHERCHER LES PRODUITS ===========================================

def rechercher_produit():

    nom = input("nom du produit à rechercher : ")

    sql = "select * from produits where nom like %s"

    curseur.execute (sql,("%" + nom + "%",))

    produits = curseur.fetchall()

    if produits:

        for p in produits:

            print(f"id: {p[0]} | Nom: {p[1]} | Catégorie: {p[2]} | Prix: {p[3]} | Quantité: {p[4]}")
    else:
        print ("aucun produit trouvé.")    

#=================================================LA FONCTION POUR SUPPRIMER LES PRODUITS ============================#
def supprimer_produits ():

    id_produit = int(input("id du produit à supprimer : "))

    sql = "delete from produits where id = %s"

    curseur.execute(sql,(id_produit,))

    conn.commit()

    print("produit supprime ")

#==============================================================LA FONCTION POUR LA VISUALITION DES PRODUITS============================#

def dashboard ():

    curseur.execute("select count(*) from produits")

    total_produits = curseur.fetchone()[0]

    curseur.execute("select SUM(quantite) from produits")

    total_stock = curseur.fetchone()[0]

    curseur.execute("SELECT SUM(prix * quantite) FROM produits")

    valeur_stock = curseur.fetchone()[0]

    print("\n DASHBOARD")

    print(f"Nombre total de produits : {total_produits}")

    print(f"Quantité totale en stock : {total_stock}")

    print(f"Valeur totale du stock : {valeur_stock} FCFA")




#===================================LE MENU POUR LE PROGRAMME =======================================
def menu ():

    print("""
          
    1.Ajouter un produit
    2.Lister l'inventaire
    3.Mettre à jour le stock
    4.Rechercher un produit
    5.Supprimer un produit
    6.Dashboard
    7.quitter                                    

    """)
menu()   

def main():
    while True:
        
        

        choix = input ("choisi une option: ")

        if choix =="1":
            Ajouter_produit ()

        elif choix == "2":
            liste_inventaire ()

        elif choix == "3":  
            Mettre_a_jour()  

        elif choix == "4":
            rechercher_produit()

        elif choix == "5":
            supprimer_produits ()

        elif choix == "6":
            dashboard ()

        elif choix == "7":
            

            print ("au revoir")
            break

        else:
            print("choix invalide")
                           
main()

    





