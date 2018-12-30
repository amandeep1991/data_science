from nltk.corpus import wordnet as wn

panda = ws.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
list(panda.closure(hyper))