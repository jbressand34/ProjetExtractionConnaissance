

source = open("dataResult2.txt","r")
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
	output = output + " "+ token2
	
	if ligne.split("\t")[0]=="SENT":
		destination.write(output+"\n")
		output = ""
source.close()
destination.close()