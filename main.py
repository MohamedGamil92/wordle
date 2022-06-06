import random
lang = "0"
print("Which language ?")
while lang not in ("1", "2", "3"):
    print("[1] English | [2] Francais")
    lang = input()
    if lang == "1": 
        with open('dictionnaireen.txt') as f:
            dictio = [line.rstrip('\n') for line in f]
    elif lang == "2":
        with open('dictionnairefr.txt') as f:
            dictio = [line.rstrip('\n') for line in f]
    elif lang == "3":
        with open('dictiotest.txt') as f:
            dictio = [line.rstrip('\n') for line in f]
    else:
        print("pine ta mams on a dit 1 ou 2: ")
print("Bienvenu sur le wordle !\nentrez 'help' pour voir les lettres non utilisées\nentrez 'show' pour voir la réponse")
dictio = [each_string.lower() for each_string in dictio]
answer = random.choice(dictio)
replist = list(answer)
tentative = ""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nombre = 1 
lemot = ['_','_','_','_','_']
orange = []
while tentative != answer:
    tentative = input("Go: ")
    tentative = tentative.lower()
    esslist = list(tentative)
    if tentative == "help": 
        print(alphabet)
    elif tentative == "show":
        print(answer)
    elif tentative in dictio:
        print('Tentative n°%d' %nombre)
        nombre = nombre + 1 
        for i in range(5):
            if esslist[i] in alphabet:
                alphabet.remove(esslist[i])
            if esslist[i]==replist[i]:
                lemot[i] = esslist[i]
                if lemot[i] not in orange:
                    orange.append(replist[i])
            else:
                for n in range(5):
                    if esslist[i] in alphabet:
                        alphabet.remove(esslist[i])
                    if esslist[i]==replist[n]:
                        if replist[n] not in orange:
                            orange.append(replist[n])
        print(*lemot, sep="")
        print(*orange, sep=", ")
    else:
        print("pas bon mot! ")
print("GG ! il t'a fallu",nombre,"essais")