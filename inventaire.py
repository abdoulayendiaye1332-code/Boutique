import mysql.connector
import hashlib


#connexion a la base de données

conn = mysql.connector.connect(

    host = "localhost",                    #  ========  Adresse du serveur MySQL =======
    user ="root",                            # ========= Nom d'utilisateur MySQL =========
    password = "Sante@2026",                   # ========== Mot de passe MySQL===============
    database= "Boutique_du_quartier"            # ==========  Nom de la base de données==================
)

curseur = conn.cursor()         # Création du curseur pour exécuter les requêtes SQL

def securite(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()
    
    
def authentification():
  while True:  
        choix = input("""
            1.se connecter
            2.inscription
            0.annuler
            """)
        if choix =="1":
            connexion ()
        elif choix =="2": 
            inscription ()
        else:
            print("choix invalide")      
        
    

#====================================INSCRIPTION=============================================#

def inscription ():
    
    nom = input("nom: ")
    prenom = input("prenom: ")
    email = input("email: ")
    mot_de_passe = input ("mot_de_passe: ")
    mot_de_passe_hash = securite(mot_de_passe)
    user="insert into utilisateurs (prenom , nom , email ,mot_de_passe) values (%s, %s, %s, %s)" 
    role = input("choisir un role")
    if role not in ("admin","utilisateur_simple"):
        print("role invalide")
    curseur.execute(user,(prenom,nom,email,mot_de_passe_hash))
    
    conn.commit()
    main()
    
#========================================CONNEXiON=============================================#


def connexion ():
    
    email = input("veuillez entrer votre email: ")
    
    mot_de_passe = input("veuillez entrer votre mot de passe: ")
    mot_de_passe_hash = securite(mot_de_passe)
    base = "select * from utilisateurs where email =%s "
    curseur.execute(base,(email,))
    mdp=curseur.fetchone()
    
    if mot_de_passe_hash == mdp[4]:
        main()
    else:
        print("mot_de_passe invalide")    
    
   
        
         
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

    curseur.execute(sql,(nom , categorie , prix ,quantite))

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

    while True:

        id_prod = str(input("id du produit: ")).strip()

        if id_prod:
            while True:

                nouvelle_quantite = input("nouvelle quantite: ")
                
                if nouvelle_quantite.isnumeric():
                    break
                else:
                    print("quantité incorrect met le nombre")
            
            sql = "update produits set quantite = %s where id = %s"

            curseur.execute(sql,(nouvelle_quantite, id_prod))

            conn.commit()

            break

        else:
            continue
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
    1.Authentification
    2.Insciption      
    3.Ajouter un produit
    4.Lister l'inventaire
    5.Mettre à jour le stock
    6.Rechercher un produit
    7.Supprimer un produit
    8.Dashboard
    0.quitter                                    

    """)
  

def main():
    while True:
        menu() 
        

        choix = input ("choisi une option: ")
        
        if choix == "1":
            authentification()
        
        if choix == "2":
            inscription ()

        if choix =="3":
            Ajouter_produit ()

        elif choix == "4":
            liste_inventaire ()

        elif choix == "5":  
            Mettre_a_jour()  

        elif choix == "6":
            rechercher_produit()

        elif choix == "7":
            supprimer_produits ()

        elif choix == "8":
            dashboard ()

        elif choix == "0":
            

            print ("au revoir")
            break

        else:
            print("choix invalide")
                           
authentification()

    





