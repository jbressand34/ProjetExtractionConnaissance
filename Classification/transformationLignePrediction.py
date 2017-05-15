import re

source = open("./lemmesNewPrediction.txt","r")
destination = open("../naiveBayesModel/dataForPrediction/lemmesDatasetPrediction.txt", "w")
output = ""
compteur = 0

for ligne in source :
	
	motInit = ligne.split("\t")[0]
	if len(ligne.split("\t")) >2:
		tag = ligne.split("\t")[1]
		lemme = ligne.split("\t")[2].split("\n")[0]
	#print motInit + " " + tag + " "+ lemme
	if "ENDOFLINE" not in ligne:
		if tag!="DT" and tag!="IN" and tag!="PP" and tag!="DT" and tag!="TO":#lemme!="<unknown>":
			if lemme=="<unknown>":
				lemme = motInit
				lemme = re.sub(r'[^a-zA-Z0-9]', r'', lemme)
				output = output + " " + lemme
			else:	
				if output != "":
					if tag =="CD":
						if re.match("^([1-4]|[1-4][1-9]|20|30|40)$",motInit):
							lemme = "negative"
						elif re.match("^([6-9]|10|[5-9][1-9]|100|60|70|80|90)$",motInit):
							lemme = "positive"
						elif re.match("^(5|50)$",motInit):
							lemme = "neutral"
						else:
							lemme = motInit
						output = output + " " + lemme
					else:
						lemme = re.sub(r'[^a-zA-Z0-9]', r'', lemme)
						if len(lemme) > 0:
							output = output + " " + lemme	
					#print output
				else :
					output = lemme
					#print output
	else:
		destination.write(output+"\n")
		output = ""
	"""
	token = mot.split("\n")[0]
	token2 = token.split("\r")[0]
	if token2=="ENDOFLINE":
		destination.write(output+"\n")
		output = ""
                token2 = ""
        elif ligne.split("\t")[0]=="NN" or ligne.split("\t")[0]=="JJ" or  ligne.split("\t")[0][:2]=="VV":               
       	        output = output + " "+ token2
	"""
        
source.close()
destination.close()
