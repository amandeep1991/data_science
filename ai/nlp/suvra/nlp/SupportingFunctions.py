import nltk
from IPython.display import HTML

def rep_sentences(texts):
    html = []
    for text in texts:
        html.append(rep_sentence(text))
    return HTML("".join(html))


def rep_sentence(text, display_pos=True):
    html_colors = ['SkyBlue'
        , 'red'
        , 'YellowGreen'
        , 'yellow'
        , 'orange'
        , 'pink'
        , 'brown'
        , 'purple'
        , 'CadetBlue'
        , 'DarkKhaki'
        , 'DarkSalmon'
        , 'Gold'
                   ]
    doc = nlp(str(text))
    n_words = len(doc)
    unique_pos = list(set(map(lambda x: x.pos_, doc)))
    pos_to_color = {i: html_colors[unique_pos.index(i)] for i in unique_pos}
    css = ["<style>.word{font-weight:bold;}</style>"]
    for pos in unique_pos:
        css.append('<style>.{}{{background-color:{};}}</style>'.format(*[pos, pos_to_color[pos]]))
    css = "".join(css)

    html = ["<table width=100%>"]
    html.append(css)
    html.append("<tr>")
    for i in range(n_words):
        word_string = doc[i].orth_
        html.append("<td><span class='word'>{0}</span></td>".format(word_string))
    html.append("</tr>")
    if display_pos:
        html.append("<tr>")
        for i in range(n_words):
            pos = doc[i].pos_
            color = pos_to_color[pos]
            html.append("<td><span class='{0}'>{0}</span></td>".format(pos))
        html.append("</tr>")
    html = "".join(html)
    return html


def custom_tag_table(list_of_word_tag_tuples):
    html_colors = ['SkyBlue'
        , 'red'
        , 'YellowGreen'
        , 'yellow'
        , 'orange'
        , 'pink'
        , 'brown'
        , 'MediumPurple'
        , 'CadetBlue'
        , 'DarkKhaki'
        , 'DarkSalmon'
        , 'Gold'
                   ]

    n_words = len(list_of_word_tag_tuples)
    words, pos_list = zip(*list_of_word_tag_tuples)
    unique_pos = list(set([pos for pair in pos_list for pos in pair]))
    pos_to_color = {i: html_colors[unique_pos.index(i)] for i in unique_pos}
    css = ["<style>.word{font-weight:bold;}</style>"]
    for pos in unique_pos:
        css.append('<style>.{}{{background-color:{};}}</style>'.format(*[pos, pos_to_color[pos]]))
    css = "".join(css)

    html = ["<table width=100%>"]
    html.append(css)
    for i in range(n_words):
        html.append("<tr>")
        word_string = words[i]
        html.append("<td><span class='word'>{0}</span></td>".format(word_string))
        row = []
        pos_sublist = pos_list[i]
        for pos in pos_sublist:
            entry = "<span class='{0}'>{0}</span> ".format(pos)
            # print entry
            row.append(entry)
        row = "".join(row)
        html.append("<td>{}</td>".format(row))
        html.append("</tr>")
    return "".join(html)


def nltk_corpus(corpus_name):
    corpus = getattr(nltk.corpus, corpus_name)
    try:
        corpus.ensure_loaded()
    except:
        nltk.download(corpus_name)
    return corpus


# read nltk corpora
def nltk_reader(corpus_name, limit=None):
    corpus = nltk_corpus(corpus_name)
    fileids = corpus.fileids()

    if limit:
        doc_iter = (" ".join([" ".join(j) for j in corpus.sents(fileid)]) for fileid in fileids[:limit])
    else:
        doc_iter = (" ".join([" ".join(j) for j in corpus.sents(fileid)]) for fileid in fileids)
    return doc_iter


universal_tags = [
    ['Open Class Words', 'ADJ', 'adjective']
    , ['Open Class Words', 'ADV', 'adverb']
    , ['Open Class Words', 'INTJ', 'interjection']
    , ['Open Class Words', 'NOUN', 'noun']
    , ['Open Class Words', 'PROPN', 'proper noun']
    , ['Open Class Words', 'VERB', 'verb']
    , ['Closed Class Words', 'ADP', 'adposition']
    , ['Closed Class Words', 'AUX', 'auxiliary']
    , ['Closed Class Words', 'CCONJ', 'coordination conjunction']
    , ['Closed Class Words', 'DET', 'determiner']
    , ['Closed Class Words', 'NUM', 'numeral']
    , ['Closed Class Words', 'PART', 'particle']
    , ['Closed Class Words', 'PRON', 'pronoun']
    , ['Closed Class Words', 'SCONJ', 'subordinating conjection']
    , ['Other', 'PUNCT', 'punctuation']
    , ['Other', 'SYM', 'symbol']
    , ['Other', 'X', 'other']
]
tag_table = pd.DataFrame(universal_tags, columns=['Category', 'Abbrev', 'Part of Speech'])
tag_table = tag_table.set_index(['Category', 'Abbrev'])

nltk.download('tagsets')
nltk.download('universal_tagset')