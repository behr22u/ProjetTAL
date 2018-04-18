import re
import nltk


chaine1 = r"*" #texte à rechercher
chaine2 = r"#"
chaine3 = r"="
chaine4 = r"}"
chaine5 = r"|\n"
chaine6 = r"''"


modif = ""
fichier = open("Corpus_partie1.txt", "r")
for ligne in fichier:
    ligne = ligne.replace(chaine6, "")
    if not(chaine1 in ligne or chaine2 in ligne or chaine3 in ligne or chaine4 in ligne or chaine5 in ligne):
        modif += ligne
        modif = modif.replace(chaine6, "")

fichier.close()
fichier = open("Corpus_partie1_corrige.txt", "w")
fichier.write(modif)
fichier.close()


modif=""
fichier2 = open("Corpus_partie2.txt", "r")
for ligne in fichier2:
    ligne = ligne.replace(chaine6, "")
    if not(chaine1 in ligne or chaine2 in ligne or chaine3 in ligne or chaine4 in ligne or chaine5 in ligne):
        modif += ligne
        modif = modif.replace(chaine6, " ")

fichier2.close();
fichier2 = open("Corpus_partie2_corrige.txt", "w");
fichier2.write(modif);
fichier2.close();

