# pip install spacy
# python -m spacy.en.download (obselete)
# python -m spacy download en

from SupportingFunctions import *
from IPython.core.display import display, HTML
import spacy
import pandas as pd

# 1. Raw example
text = u'India is awesome'  # unicode representation has certain benifits
nlp = spacy.load('en')
doc = nlp(text)
token = doc[0]
span = doc[0:2]
print(token)
print(span)

# 2. pipeline (default)
for functions_in_pipeline in nlp.pipeline:
    print(functions_in_pipeline)


# 3. code snippet (Modifying language model)
def identify_starwars(doc):
    for token in doc:
        if token.text == u'starwars':
            token.tag_ = u'NNP'


def return_pipeline(nlp):
    return [nlp.create_pipe('tagger'), nlp.create_pipe('parser'), nlp.create_pipe('ner'), identify_starwars]


text = u'I love one plus 6 starwars edition model'
custom_nlp_model = spacy.blank('en')
print('#1')
for each_pipeline_component in return_pipeline(custom_nlp_model):
    custom_nlp_model.add_pipe(each_pipeline_component)
print('#2')
new_document = custom_nlp_model(text)
print('#3')

for functions_in_pipeline in custom_nlp_model.pipeline:
    print(functions_in_pipeline)

# 4  parallel processing:
texts = [u'Your are amazing'] * 10000
for doc in nlp.pipe(texts, n_threads=7):  # pipe returns generator object ( work kind of streams )
    print(doc.is_parsed)

# 5 multiple threads benchmarking
from datetime import datetime

import pandas as pd

runtimes = {}
for thread_count in [1, 2, 3, 4, 8]:
    t0 = datetime.now()
    processed_documents = nlp.pipe(texts, n_threads=thread_count)  # create generator of processed documents
    for doc in processed_documents:  # iterate over generator
        print(doc.is_parsed)
    t1 = datetime.now()
    runtimes[thread_count] = (t1 - t0).total_seconds()

ax = pd.Series(runtimes).plot(kind='bar')
ax.set_ylabel('Runtime (Seconds) with N threads')
plt.show()

# 6 Accessing tokens and spans in spacy
import pandas as pd


def info(obj):
    return {'type': type(obj), '__str__': str(obj)}


text = u'India is great and awesome. What about you sir? Aman is also good Indian.'
document = nlp(text)
token = document[0]
span = document[0:3]
print('Hello')
pd.DataFrame(list(map(info, [token, span, document])))
print(list(document.sents))  # document.sents returns generator, so can't call document.sents[0]
print(list(document))  # document is actually a generator for tokens
for token in document:
    print(token)
print(document)
print(type(document))
print(document[2])  # document is not purely a generator, so we can have index operations on that to get tokens at specified indexes

# 7 Morphological decomposition of token
token = document[2]
print(token)
print(token.text)
print(token.tag_)
print(token.suffix_)
print(token.lemma_)

# 8 Parts of speech and dependency tagging
attrs = map(lambda token: {
    'token'          : token,
    'parts of speech': token.pos_,
    'dependency'     : token.dep_
}, document)

print(pd.DataFrame(list(attrs)))


# 9 Noun chunking
print('Nouns chunking')
print(list(document.noun_chunks)) # document.noun_chunks returns generator


# 10 Named Entity Recognition
ents = [(ent, ent.root.ent_type_) for ent in document.ents]
print(ents)


# 11 Word vector representations
def plot_similarities(similarities, target):
    import matplotlib.pyplot as plt
    plt.show()

computer = nlp(u'computer')
document2 = nlp(u'You might be using a machine running Windows')
similarities = {}
[ similarities.update(dd) for dd in map(lambda token: {token:[token.similarity(computer)]}, document2)]
pd.DataFrame(similarities).plot(kind='bar')
# plt.show()

# 12 spacy vs nltk approach
# nltk gives functional programming approach, where word tokenizer just returns tokens but no relation between/among them
# whereas spacy uses the object-oriented approach to find the tokens with their dependency relations among tokens
# spacy objects are immutable so better performant - use string store


# 13 pos tags
document = nlp(text)
token = document[0]
print(token.pos, token.pos_)

POS_INDEX = token.pos
StringStore = token.vocab.strings
print(StringStore[POS_INDEX])

# 14 with every new doc/word size of StringStore increases
document = nlp(u'India is great and awesome. What about you sir? Aman is also good Indian.')
StringStore = document.vocab.strings
print(len(StringStore))
new_document = nlp(u'Hindustan was also cool')
StringStore = new_document.vocab.strings
print(len(StringStore)) # count increased a little


# 15 Parts of speech tags for disambiguation
sentence1 = 'I got a discount on newspaper'
sentence2 = 'I discount that newspaper'
display(rep_sentences([sentence1, sentence2]))


# 16 same word can have different parts of speech in the given set of documents collectively
from collections import defaultdict, Counter
unique_tag_dictionary = defaultdict(set)

for doc in nlp.pipe(nltk_reader('brown'), n_threads=1):
    for token in doc:
        unique_tag_dictionary[token.orth_].add(token.pos_)

#for each word, how many unique POS's were found?
n_word_senses = {word: len(senses) for word, senses in unique_tag_dictionary.items()}

# #map each word to its number of senses, and count
ambiguous_word_counts = Counter()
for doc in nlp.pipe(nltk_reader('brown'), n_threads=1):
    word_senses = map(lambda token: n_word_senses[token.orth_] , doc)
    ambiguous_word_counts.update(word_senses)

# #normalize and feed to pandas
N = float(sum(ambiguous_word_counts.values()))
plot_data = pd.Series(ambiguous_word_counts).map(lambda x: x / N)

#plot
plot_data.iplot(kind='bar'
                , title = "45% of Brown Corpus of Spacy-tagged tokens are ambiguous"
                , xTitle = "Unique Parts of Speech in Brown Corpus"
                , yTitle= "Percent of Unique Words in Vocabulary"
               )


# 17: ent
document = nlp('''India is the best country in the world today. Narender Modi is the PM of India. 
Amandeep is also a good boy. My name is Amandeep. Aman Deep is the future President of India. Amandeep is the future President of India''')
sent = next(document.sents)
for tok in sent:
    print('{} -> {}'.format(tok, tok.ent_type_))

for ent in document.ents:
    print('{} -> {}'.format(ent.string, ent.label_))

[ent for ent in document.ents if ent.label == spacy.symbols.PERSON]


# 18: token vectors
token = document[0]
print(token.vector[:25])