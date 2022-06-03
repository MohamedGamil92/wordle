import random
lang = "0"
print("Which language ?")
while lang not in ("1", "2"):
	print("[1] English | [2] Francais ")
	lang = input()
	if lang == "1":
		with open('dictionnaire.txt') as f:
			dictio = [line.rstrip('\n') for line in f]
	elif lang == "2":
		with open('dictionnaire.txt') as f:
			dictio = [line.rstrip('\n') for line in f]
	else:
		print("pine ta mams on a dit 1 ou 2: ")
answer = random.choice(dictio)
answer = answer.lower()
replist = list(answer)
tentative = input("Mot ? ")
tentative = tentative.lower()
esslist = list(tentative)
nombre = 1 
lemot = ['_','_','_','_','_']
orange = []
while tentative != answer:
    if tentative == "zzzzz":
        print(answer)
        tentative = input("Tricheur ! ")
        tentative = tentative.lower()
        esslist = list(tentative)
    elif tentative in dictio:
        print('Tentative n°%d' %nombre)
        nombre = nombre + 1 
        for i in range(5):
            if esslist[i]==replist[i]:
                lemot[i] = esslist[i]
            else:
                for n in range(5):
                    if esslist[i]==replist[n]:
                        if replist[n] not in orange:
                            orange.append(replist[n])
        print(*lemot, sep="")
        print(*orange, sep=", ")
        tentative = input("Nouvelle tentative ? ")
        tentative = tentative.lower()
        esslist = list(tentative)
    else:
        tentative = input("pas bon mot! ")
        tentative = tentative.lower()
        esslist = list(tentative)
print("GG ! il t'a fallu",nombre,"essais")