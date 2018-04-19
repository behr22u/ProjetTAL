import xml.etree.ElementTree as ET
from pprint import pprint
from nltk.corpus import wordnet as wn


tree = ET.parse('Corpus_partie1.txt.xml')
#tree = ET.parse('Corpus_partie2.txt.xml')
root = tree.getroot()



def getLocation(sentence):
    location = []
    tokens = sentence.findall('tokens/token')
    for token in tokens:
        loc = token.find('NER')
        if loc.text == 'LOCATION':
            location.append(token.find('word').text)

    return location



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

    return names


def getNames(sentence):
    names = []
    print("boucles sentence")
    tokens = sentence.findall('tokens/token')
    for token in tokens:
        person = token.find('NER')
        if person.text == 'PERSON':
            names.append(token.find('word').text)


    return names


def getDates(sentence):
    dates = []
    print("boucles sentence")
    tokens = sentence.findall('tokens/token')
    for token in tokens:
        date = token.find('NER')
        if date.text == 'DATE':
            dates.append(token.find('Timex').text)

    return dates






def getSentencesWithKillAndNameV3(): # retourne les phrases qui comportent un nom et kill et la hrase suivante puis on les affiche
    i = 0 #nombre de phrase trouvées
    checkSentence = True;
    nbSentences = 0;
    ourSentences = []
    sentences = root.findall('document/sentences/sentence')
    print("boucle sentence")
    for sentence in sentences:
        if(checkSentence ):  # on rajoute une phrase parce que elle contient un nom et kill
            hasName = doesThisSentenceHasAName(sentence)
            hasKill = doesThisSentenceHasAKill(sentence)
            if(hasName and hasKill):
                ourSentences.append(sentence)

                names = getNames(sentence)
                locs = getLocation(sentence)
                dates = getDates(sentence)
                ourSentences.append(names + locs + dates)

                i = i+1
                checkSentence = False;
                nbSentences = 2;
        else:
            # on rajoute une phrase parce-qu'elle suit une phrases contenant un nom et kill
            ourSentences.append(sentence)
            names = getNames(sentence)
            locs = getLocation(sentence)
            dates = getDates(sentence)
            ourSentences.append(names + locs + dates)

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
    bool = True
    for s in ourSentences :
        if(bool):
            print("")
            tokens = s.findall('tokens/token')
            mySentence = ""
            for token in tokens:
                mySentence = mySentence + " " + token.find('word').text
            print(mySentence)
            bool = False
        else:
            print("")
            mySentence = ""
            for token in s:
                if(token != None):
                    mySentence = mySentence + " " + token
            print(mySentence)
            bool = True
    print(i)
    return ourSentences




def getListSynonyms(): # renvoie une liste de synonymes du mot kill
    tabOfSynonym = []
    killSyn = wn.synset('kill.n.01')
    for a in killSyn.hyponyms():
          tabOfSynonym.append(a.name().split(".")[0].replace('_',' '))
    return tabOfSynonym

def getSentencesWithKillAndNameV4(): # renvoie les id des phrases trouvées
    i = 0 #nombre de phrase trouvées
    checkSentence = True;
    nbSentences = 0;
    ourSentences = []
    sentences = root.findall('document/sentences/sentence')
    print("boucle sentence")
    for sentence in sentences:
        if(checkSentence ):  # on rajoute une phrase parce que elle contient un nom et kill
            hasName = doesThisSentenceHasAName(sentence)
            hasKill = doesThisSentenceHasAKill(sentence)
            if(hasName and hasKill):
                ourSentences.append(sentence.attrib['id'])
                i = i+1
                checkSentence = False;
                nbSentences = 2;
        else:
            # on rajoute une phrase parce que elle suit une phrases contenant un nom et kill
            ourSentences.append(sentence.attrib['id'])
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
            print(s)
    return ourSentences


def getDependent(word):#prend en parametres un mot gouvernor et renvoie les mots dépendants
    dependants = []
    sentences = root.findall('document/sentences/sentence')
    print("boucle dep")
    for sentence in sentences:
        dependenciesList = sentence.findall('dependencies')
        for dependencies in dependenciesList :
            typeDep = dependencies.attrib['type']
            if ( typeDep == 'basic-dependencies' ):
                depList = dependencies.findall('dep')
                for dep in depList:
                    #attribut = dep.attrib['type']
                    #print(attribut)
                    gouv = dep.find('governor')
                    if gouv.text == word:
                        dependants.append(dep.find('dependent').text)
    print('Liste de tous les mots')
    for dep in dependants:
        print(dep)

def getDependentBySentenceID(word, id):#prend en parametres un mot gouvernor et renvoie les mots dépendants
    dependants = []
    sentences = root.findall('document/sentences/sentence')
    print("boucle dep")
    for sentence in sentences:
        if( sentence.attrib['id'] == id ):
            dependenciesList = sentence.findall('dependencies')
            for dependencies in dependenciesList :
                typeDep = dependencies.attrib['type']
                if ( typeDep == 'basic-dependencies' ):
                    depList = dependencies.findall('dep')
                    for dep in depList:
                        #attribut = dep.attrib['type']
                        #print(attribut)
                        gouv = dep.find('governor')
                        if gouv.text == word:
                            dependants.append(dep.find('dependent').text)
    print('Liste de tous les mots')
    for dep in dependants:
        print(dep)

def getGovernor(word):#prend en parametres un mot dependent et renvoie les mots governor
    dependants = []
    sentences = root.findall('document/sentences/sentence')
    print("boucle dep")
    for sentence in sentences:
        dependenciesList = sentence.findall('dependencies')
        for dependencies in dependenciesList :
            typeDep = dependencies.attrib['type']
            if ( typeDep == 'basic-dependencies' ):
                depList = dependencies.findall('dep')
                for dep in depList:
                    #attribut = dep.attrib['type']
                    #print(attribut)
                    gouv = dep.find('dependent')
                    if gouv.text == word:
                        dependants.append(dep.find('governor').text)
    print('Liste de tous les mots')
    for dep in dependants:
        print(dep)

getSentencesWithKillAndNameV3()
