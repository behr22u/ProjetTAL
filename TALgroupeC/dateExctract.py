import xml.etree.ElementTree as ET
from pprint import pprint
#tree = ET.parse('corpusTalV1.txt.xml')
#tree = ET.parse('exempleTuto.xml')
tree = ET.parse('../Corpus_partie1.txt.xml')
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


def test():
    # chargement données
    tree = ET.parse('corpusTalV1.txt.xml')
    for child in root:
        theTrueRoot = child
        #pprint(theTrueRoot.tag) nnp
        exemples = root.findall('kill')

    pprint("before the loop")

    # pour chaque phrases dans le document
    #   si une phrase à un POS égal NNP
    #       afficher la phrase

    i = 0
    for sentence in theTrueRoot.iter('sentence'):
        for pos in sentence.iter('POS'):
            if (pos.text == 'NNP'):
                listPhrase = []
                for words in sentence:
                    pprint(words.text)



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
            ourSentences.append(sentence)

    print('Liste des phrases avec des personnes commançant par C et des dates')
    for s in ourSentences :
        tokens = s.findall('tokens/token')
        for token in tokens:
            print(token.find('word').text)

    return ourSentences

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

getSentencesWithKillAndName()