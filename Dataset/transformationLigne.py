

source = open("dataset3.txt","r")
destination = open("lemmesLignes.txt", "wt")
output = ""


a = "hello"
b = "world"
a += b
print a

for ligne in source:
	mot = ligne.split("\t")[1] 
	token = mot.split("\n")[0]
	token2 = token.split("\r")[0]
	if( token2 != "ENDOFLINE"):
		output = output + " "+ token2
	
	if token2 =="ENDOFLINE":
		destination.write(output+"\n")
		output = ""
source.close()
destination.close()