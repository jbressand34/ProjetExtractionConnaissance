#!/usr/bin/env python3
#-*- coding: utf-8 -*

import os
import re
import subprocess

 


os.system("clear")
choix = input("Voulez-vous faire un apprentissage?[O/N)\n (Il est necessaire d'en avoir fait au moins un pour la suite)\n")
if (choix == "O"):

	print("DATASETS disponibles pour l'apprentissage:")
	os.system("ls ../Dataset")
	print("\n")

	nomDataset = input("Choisissez le DATASET à traiter(de la forme [a-zA-Z0-9_-]+\.txt):\n")
	#if re.match(r"[a-zA-Z0-9_-]+\.txt", nomDataset):
	nomDataset = "../Dataset/"+nomDataset

	print("Traitements en cours...\n")

	os.system("cat "+nomDataset+" | cmd/tree-tagger-english > ./lemmesNew.txt")

	print("TreeTagger terminé\nReconstitution du dataset lemmatisé...\n")
	os.system("python3 ./transformationLigne.py")
	print("Done\n")

#os.system("ls ../naiveBayesModel/dataForTraining/")

	print("Lancement des prétraitements Weka...\n")
	os.system("python3 ../naiveBayesModel/pretraitementDonneesEntrainement.py")
	print("Done\n")

	print("Lancement de l'apprentissage et construction du model...")
	os.system("python3 ../naiveBayesModel/constructionModel.py")
	print("Done\n")
	os.system("ls ../naiveBayesModel/models")
	print("\n")

#### Test###
choix = input("Voulez-vous faire un Test du modèle?[O/N]\n")
if (choix == "O"):
	###TreeTagger dataset test###
	print("\n")
	print("DATASETS disponibles pour les tests:\n")
	os.system("ls ../naiveBayesModel/dataForTesting")
	print("\n")
	nomDataset = input("Choisissez le DATASET à traiter (de la forme [a-zA-Z0-9_-]+\.txt):\n")
	if re.match(r"[a-zA-Z0-9_-]+\.txt", nomDataset):
		nomDataset = "../naiveBayesModel/dataForTesting/"+nomDataset

	print("Traitements en cours...\n")	

	os.system("cat "+nomDataset+" | cmd/tree-tagger-english > ./lemmesNewTest.txt")

	print("TreeTagger terminé\nReconstitution du dataset lemmatisé...\n")
	os.system("python3 ./transformationLigneTest.py")
	print("Done\n")


	os.system("python3 ../naiveBayesModel/pretraitementDonneesTest.py")
	print("Done\n")

	print("Lancement du test...")
	os.system("python3 ../naiveBayesModel/modelTest.py")
	print("Done\n")


choix = input("Voulez-vous faire une prédiction?[O/N]\n")

if (choix == "O"):
	os.system("python3 ../naiveBayesModel/pretraitementDonneesPrediction.py")
	print("Done\n")

	print("Lancement de la classification...")
	os.system("python3 ../naiveBayesModel/modelPediction.py")
	print("Done\n")
	print("Convertissement du résultat...")
	os.system("python3 ../naiveBayesModel/transformResultIntoCSV.py")
	print("Done\n")


