import mysql.connector as sqlbdd
import random
from datetime import datetime


mybdd = sqlbdd.connect(
    host="localhost",  
    user="root",  
    passwd="example",  
    db="etudiant",
    port="3307")  

print("Connection réussie")
cursor = mybdd.cursor()

#Récuperer la table apprenants dans la base de donnée et les afficher :


query = "SELECT id, prenom_eleve, nom_eleve FROM liste_etudiant"

cursor.execute(query)
liste_etudiant = []

for identifiant, prenom, nom in cursor :
    personne = [identifiant, prenom, nom]
    liste_etudiant.append(personne)


print("Voici la liste des etudiants :\n", liste_etudiant)

#fonction qui permet d'executer la creation de groupe en fonction du nombre de 
#personnes souhaité dans le groupe !


nombre_personne_par_groupe = int(input("Combien de personnes par groupe ?"))
groupes = []

def groupe_eleve(liste):
    global nombre_personne_par_groupe
    global groupes
    random.shuffle(liste)

    while liste != []:
        restant = len(liste)%nombre_personne_par_groupe
        if restant == 0:
            groupes.append(liste[0:nombre_personne_par_groupe])
            del liste[0:nombre_personne_par_groupe]
        else:
            groupes.append(liste[0:restant])
            del liste[0:restant]
    return groupes

groupe_eleve(liste_etudiant)

# affichage des groupes en fonction de la demande de l'utilisateur

print("Voici les groupes :")
numero_de_groupe = 0
for groupe in groupes:
    numero_de_groupe += 1
    affichage_groupes = ''.join(' - '.join([str(elem) for elem in groupe]))
    affichage_groupes = affichage_groupes.replace('[','').replace(']','').replace("'",'')
    print( f"Groupe {numero_de_groupe} = {affichage_groupes}")


cursor.close()
mybdd.close()