from xml.etree import ElementTree as ET
from pprint import pprint


#chargement données
tree = ET.parse('Corpus_partie1.txt.xml')
root = tree.getroot()
for child in root : 
    theTrueRoot =  child
#pprint(theTrueRoot.tag) nnp
#exemples = root.findall('kill')

pprint("before the loop")
i = 0
for child in theTrueRoot.iter('POS') :
    if(child.text == 'NNP') :
        pprint(child.text)
