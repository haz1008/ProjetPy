import sys
import re
import sys
import re 
#Version 1:
def lect_VCF(file): 
    dico_données={} #stocke les données extraite du fichier VCF sous forme position:sequence
    print("Processing file: "+file)
    
    with open(file, 'r') as fichier:
        for line in fichier :
            if not line.startswith('#'):
                info=line.strip().split("\t")  #transforme chaque ligne du fichier VCF en une liste
                #puisque les infos d'une ligne sont séparés par des tabulations 
                position= info[1]  #la position est le 2eme element de la ligne
                sequence=info[4]   #la sequence est le 5eme element de la ligne
                colonne_8=info[7].strip().split(";") #la colonne 8 est separée par des ; 
                svlen=colonne_8[2].strip().split("=") [1]  #svlen est le 2eme element de la colonne8, et sous forme de clef=valeur
                
                #Pour fusionner les doublouns de variants sur une meme position en fct de svlen:
                valeur=[sequence, svlen] #stockage temporaire des seq avec leurs svlen ds une liste
                if position in dico_données:  #Si position (clef de dico_données) existe deja dans dico_données 
                    #print("La position: "+position + " existe déjà")
                    if dico_données[position][1] < svlen:  # Si svlen de la sequence actuelle (svlen) est sup à celle déjà stocké ds dico sur cette meme position
                        dico_données[position]=valeur
                        #print("valeur")
                        
                else:
                    #print("La position "+position +  " doit etre ajoutée")
                    dico_données[position]=valeur #Si on a pas une clef pour cette position, on la cree et on lui affecte la valeur

    for position in dico_données: #pour enlever svlen du dico_données
        dico_données[position]=dico_données[position][0] #on ecrase [seq,svlen] par la valeur à la position 0: seq
    return dico_données

def dupl_v1(dico_ech): #prend le nom du dico externe comme argument (P15 ou P30)
    liste_v1=[]
    liste_rep=list(dico_ech.keys()) #crée une liste des clefs du dico externe (=> P15-1, P15-2, P15-3)
    pdb=0 #la difference de position en pdb entre deux duplicats
    for i in range(len(liste_rep)): #boucle externe iteration sur les elements de la liste de replicats
        for j in range(i+1, len(liste_rep)): #boucle interne: iteration sur la meme liste à indice i+1
            dico1=dico_ech[liste_rep[i]] #stockage temporarire des elements (clés de chaque dico réplicats) de la liste_rep
            dico2=dico_ech[liste_rep[j]]
            for pos1,seq1 in dico1.items(): #boucle a iteration sur chaque pos et seq dans le dico1
                for pos2,seq2 in dico2.items():
                    if seq1==seq2 and (int(pos1)-pdb <= int(pos2) <= int(pos1) +pdb): #la difference entre les sequences doit etre +-10
                        if (seq1=="<DEL>" or seq1=="<INS>" or seq1=="<DUP>") and (seq2=="<DEL>" or seq2=="<INS>" or seq2=="<DUP>"):
                            print("Impossible de comparer.")
                        else:
                            liste_v1.append(seq1)
    return liste_v1

#Version 2:
def dupl_var(dico_ech): 
    pdb=10 
    liste_var=dupl_v1(dico_ech)
    return liste_var