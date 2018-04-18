# On importe les fonctions de tokenisation de mots, de POS-Tagging et de reconnaissance d'entités de NLTK
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

f = open('Corpus_partie1.txt', 'r')
i = 0
print("début")
for line in f:

    i = i+1

    if(i < 10):
        print("yo")
        print(line)
        type(line)
        text_en = line

        # On tokenise la phrase
        tokens_en = word_tokenize(text_en)

        # On tague les tokens
        tags_en = pos_tag(tokens_en)

        # On applique la fonction de reconnaissance d’entités
        chunked = ne_chunk(tags_en)

        for name in chunked:

            print (name)
    else:
        break

