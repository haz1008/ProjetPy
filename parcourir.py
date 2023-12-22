import os, sys
import compare
os.system

liste_VCF=[]
def parcours (repertoire): 
    #print("Je suis dans " +repertoire)
    
    list_rep=os.listdir(repertoire)
    
    for file in list_rep: #Verifie si le file est un dossier, et si on a acces pour l'executer
        
        path_file=os.path.join(repertoire, file) #os.path.join combine le chemin rep et le nom file
        
        if os.path.isdir(path_file): #le chemin du file present ds le repertoire
            #print(path_file + "est un dossier")
            if os.access(path_file, os.X_OK): #nécessaire pour vérifier si on a acces aux sous-dossier
                parcours(path_file)           #parcours: fct récursive
        else:
            extension=file.split(".")[-1]
            if extension=="vcf":
                liste_VCF.append(path_file)

parcours(sys.argv[1]) #etape 1: appel de la fct parcours
#print(liste_VCF)

echantillon={} #dictionnaire de l'echantillon contenant des sous-dico (réplicats)
def ajout_echantillon(nom_replicat, dico_données): #prend une variable contenant le nom du replicat, et un dictionnaire de donnees du fichier vcf en arguments. 
    if nom_replicat in echantillon:   # vérifie si l'échantillon existe déjà dans le dico echantillon
        for position, sequence in dico_données.items():
            echantillon[nom_replicat][position] = sequence #ajoute la position (cle du dico replicat) et la sequence au dictionnaire
    else:
        echantillon[nom_replicat] = dico_données  #crée un nouveau dictionnaire pour le replicat s'il n'existe pas deja

for path_file in liste_VCF:
    sous_dico=path_file.split("/")[-1].split(".")[0] #split / se fait entre chemin rep et chemin file
    #print(sous_dico)
    if sous_dico.startswith("P15"):
        #print("TEST2")
        echantillon[sous_dico]=compare.lect_VCF(path_file) #fct qui rend un dico
        #la clef de P15 sous_dico: prend comme valeur un dico
        liste_v1_P15=compare.dupl_v1(echantillon)
        print(liste_v1_P15) #preciser entre quel rep
        liste_v2_P15=compare.dupl_var(echantillon)
        
        print(liste_v2_P15)

    if sous_dico.startswith("P30"):
        echantillon[sous_dico]=compare.lect_VCF(path_file)
        liste_v1_P30=compare.dupl_v1(echantillon)
        print(liste_v1_P30)
        liste_v2_P30=compare.dupl_var(echantillon)
        print(liste_v2_P30)
#print(P15)
#print(P30)
print("Version 1:  Le nombre de variants dupliqués dans l'échantillon P15: " + str(len(liste_v1_P15))) 
print("Version 1:  Le nombre de variants dupliqués dans l'échantillon P30: " + str(len(liste_v1_P30)))

print("Version 2: Le nombre de variants dupliqués dans l'échantillon P15: " + str(len(liste_v2_P15)))
print("Version 2: Le nombre de variants dupliqués dans l'échantillon P30: " + str(len(liste_v2_P30)))


