import xml.etree.ElementTree as ET
from pprint import pprint
#tree = ET.parse('corpusTalV1.txt.xml')
#tree = ET.parse('exempleTuto.xml')
tree = ET.parse('Corpus_partie1_corrige.txt.xml')
root = tree.getroot()



#chargement données
def extractNE(tree):
    pprint("debug1")
    root = tree.getroot()
    pprint("debug1")
    exemples = root.findall('kill')
    pprint("debug1")
    for each in exemples :
        pprint(each)





def getNamesAndDates():
    names = []
    sentences = root.findall('document/sentences/sentence') #Peut etre besoin de remplacer par 'document/sentence/sentence'
    print("boucle sentence")
    for sentence in sentences :
        tokens=sentence.findall('tokens/token')
        for token in tokens :
            person = token.find('NER')
            if person.text == 'PERSON':
                name = token.find('word').text
                if name[0] == 'C' :
                    names.append(name)
                    tokens = sentence.findall('tokens/token')
                    for token in tokens:
                        aDate = token.find('NER')
                        if aDate.text == 'DATE':
                            date = token.find('word').text
                            print("it's a date")
                            names.append(date)

    print('Liste de personnes commençant par C')
    for name in names :
        print(name)
    return names

def getSentencesWithKillAndName():
    i = 0
    ourSentences = []
    sentences = root.findall('document/sentences/sentence') #Peut etre besoin de remplacer par 'document/sentence/sentence'
    print("boucle sentence")
    for sentence in sentences :
        hasName = False
        hasKill = False
        tokens=sentence.findall('tokens/token')
#################################################
        for token in tokens :
            person = token.find('NER')
            if person.text == 'PERSON':
                name = token.find('word').text
                if name[0] == 'C' :
                    hasName = True

###########################################################
            kill = token.find('word').text
            if kill == 'kill':
                hasKill = True
        if(hasName and hasKill):
            i = i+1
            ourSentences.append(sentence)


    print('Liste des phrases avec des personnes commançant par C et des dates')
    for s in ourSentences :
        tokens = s.findall('tokens/token')
        for token in tokens:
            print(token.find('word').text)

    return ourSentences


def doesThisSentenceHasAName(sentence):
    tokens = sentence.findall('tokens/token')
    hasName = False
    for token in tokens:
        person = token.find('NER')
        if person.text == 'PERSON':
            name = token.find('word').text
            if name[0] == 'C':
                hasName = True
    return hasName


def doesThisSentenceHasAKill(sentence):
    tokens = sentence.findall('tokens/token')
    hasKill = False
    for token in tokens:
        kill = token.find('word').text
        if kill == 'kill':
            hasKill = True
    return hasKill


def getNames():
    names = []
    sentences = root.findall('document/sentences/sentence')  # Peut etre besoin de remplacer par 'document/sentence/sentence'
    print("boucle sentence")
    for sentence in sentences:
        tokens = sentence.findall('tokens/token')
        for token in tokens:
            person = token.find('NER')
            if person.text == 'PERSON':
                names.append(token.find('word').text)
    print('Liste de tous les noms')
    for name in names:
        print(name)
    return names


def getSentencesWithKillAndNameV2():
    i = 0
    ourSentences = []
    sentences = root.findall('document/sentences/sentence') #Peut etre besoin de remplacer par 'document/sentence/sentence'
    print("boucle sentence")
    for sentence in sentences :
        hasName = doesThisSentenceHasAName(sentence)
        hasKill = doesThisSentenceHasAKill(sentence)
        if(hasName and hasKill):
            ourSentences.append(sentence)
            i = i+1


    print('Liste des phrases avec des personnes commançant par C et des dates')
    for s in ourSentences :
        tokens = s.findall('tokens/token')
        for token in tokens:
            print(token.find('word').text)
    print(i)
    return ourSentences




def getSentencesWithKillAndNameV3():
    i = 0 #nombre de phrase trouvées
    checkSentence = True;
    nbSentences = 0;
    ourSentences = []
    sentences = root.findall('document/sentences/sentence') #Peut etre besoin de remplacer par 'document/sentence/sentence'
    print("boucle sentence")
    for sentence in sentences:
        if(checkSentence ):  # on rajoute une phrase parce que elle contient un nom et kill
            hasName = doesThisSentenceHasAName(sentence)
            hasKill = doesThisSentenceHasAKill(sentence)
            if(hasName and hasKill):
                ourSentences.append(sentence)
                i = i+1
                checkSentence = False;
                nbSentences = 2;
        else:
            # on rajoute une phrase parce que elle suit une phrases contenant un nom et kill
            ourSentences.append(sentence)
            
            hasName = doesThisSentenceHasAName(sentence)
            hasKill = doesThisSentenceHasAKill(sentence)
            if (hasName and hasKill):
                nbSentences = 2;
            else:
                if(nbSentences == 0):
                    checkSentence = True;
                else:
                    nbSentences = nbSentences - 1;





    print('Liste des phrases avec des personnes commançant par C et des dates')
    for s in ourSentences :
        tokens = s.findall('tokens/token')
        for token in tokens:
            print(token.find('word').text)
    print(i)
    return ourSentences


#getSentencesWithKillAndName() meme nombre de phrases trouvés yes
#getSentencesWithKillAndNameV2()
getSentencesWithKillAndNameV3()