from xml.etree.ElementTree import ElementTree as ET
from pprint import pprint

tree = ET.parse('corpusTalV1.txt.xml')

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
    from xml.etree import ElementTree as ET
    from pprint import pprint

    # chargement données
    tree = ET.parse('corpusTalV1.txt.xml')
    root = tree.getroot()
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

test()