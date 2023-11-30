import os, sys
import compare
os.system

liste_VCF=[]
def parcours (repertoire):  #repertoire: stocke le chemin donné en argument ds l'etape 1
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

P15={}
P30={}

for path_file in liste_VCF:
    sous_dico=path_file.split("/")[-1].split(".")[0] #split / se fait entre chemin rep et chemin file
    #print(sous_dico)
    if sous_dico.startswith("P15"):
        #print("TEST2")
        P15[sous_dico]=compare.lect_VCF(path_file) #fct qui rend un dico
        #la clef de P15 sous_dico: prend comme valeur un dico
        liste_v1_P15=compare.dupl_v1(P15)
        liste_v2_P15=compare.dupl_var(P15)
        print(len(liste_v1_P15))
        print(liste_v2_P15)

    if sous_dico.startswith("P30"):
        P30[sous_dico]=compare.lect_VCF(path_file)
        liste_v1_P30=compare.dupl_v1(P30)
        liste_v2_P30=compare.dupl_var(P30)

#print(P15)
#print(P30)
print("Version 1:  Le nombre de variants dupliqués dans l'échantillon P15: " + str(len(liste_v1_P15)))
print("Version 1:  Le nombre de variants dupliqués dans l'échantillon P30: " + str(len(liste_v1_P30)))

print("Version 2: Le nombre de variants dupliqués dans l'échantillon P15: " + str(len(liste_v2_P15)))
print("Version 2: Le nombre de variants dupliqués dans l'échantillon P30: " + str(len(liste_v2_P30)))


