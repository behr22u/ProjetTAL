import xml.etree.ElementTree as ET
from pprint import pprint
#tree = ET.parse('corpusTalV1.txt.xml')
#tree = ET.parse('exempleTuto.xml')
tree = ET.parse('Corpus_partie1.txt.xml')
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

def testLea():
    print("lancement du test!");
    root = tree.getroot()

    for child in root:
        pprint(child.tag)
    print("sortie de boucle");

def algoProf():
    exemples = root.findall('exemple');
    for eatch in exemples:
        attrib1 = eatch.attrib['attrib']<root><exemple attrib1 ="">.<phrase>'That is ..'</phrase></exemple>
        phrase_test = eatch.find('phrase').text</root>

def getNamesByC():
    names = []
    sentences = root.findall('document/sentences/sentence') #Peut etre besoin de remplacer par 'document/sentence/sentence'
    print("boucle sentence")
    for sentence in sentences :
        tokens=sentence.findall('tokens/token')
        for token in tokens :
            person = token.find('NER')
            if person.text == 'PERSON' :
                name = token.find('word').text
                if name[0] == 'C' :
                    names.append(name)
    print('Liste de personnes commençant par C')
    for name in names :
        print(name)
    return names

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

getNamesByC()