import xml.etree.ElementTree as ET
from pprint import pprint
from nltk.corpus import wordnet as wn
#tree = ET.parse('corpusTalV1.txt.xml')
#tree = ET.parse('exempleTuto.xml')


tree = ET.parse('Corpus_partie1_corrige.txt.xml')
root = tree.getroot()



def getLocation(sentence):
    location = []
    sentences = root.findall('document/sentences/sentence')  # Peut etre besoin de remplacer par 'document/sentence/sentence'
    print("boucle sentence")
    for sentence in sentences:
        tokens = sentence.findall('tokens/token')
        for token in tokens:
            loc = token.find('NER')
            if loc.text == 'LOCATION':
                location.append(token.find('word').text)
    print('Liste de tous les localisations')
    for loc in location:
        print(loc)
    return location



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
        kill = token.find('lemma').text
        if kill in getListSynonyms():
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



def dictionaryOfKill():
     wordnet.synset('small')



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

    print('Liste des phrases avec des personnes commançant par C et des kills')
    for s in ourSentences :
        tokens = s.findall('tokens/token')
        mySentence = ""
        for token in tokens:
            mySentence = mySentence + " " + token.find('word').text
        print(mySentence)
    print(i)
    return ourSentences




def getListSynonyms():
    tabOfSynonym = []
    killSyn = wn.synset('kill.n.01')
    for a in killSyn.hyponyms():
          tabOfSynonym.append(a.name().split(".")[0].replace('_',' '))
    return tabOfSynonym


getSentencesWithKillAndNameV3()