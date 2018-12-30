# Natural Language Processing using NLTK

# Install NLTK - pip install nltk

# Tokenization of paragraphs/sentences
import nltk

# paragraph = """The Taj Mahal was built by Emperor Shah Jahan in 1970 at 10:20 A.M."""

paragraph = """Vodafone UK - Technology Operations
Planned Maintenance Notice
 
Dear CAP GEMINI, 

Please be advised that the Planned Works have been Completed: CRQ000000914975 

Detailed Description of Works:
Third party will be performing mandatory cable works on their fiber optical network, Germany . 

Scheduled Start/End Date & Outage Window:
04 August 2018 22:00 Hours GMT to 05 August 2018 04:00 Hours GMT 

Impact Assessment:
Loss of Service for 06 hours 

Contingency Date:
NA 
"""
               
# POS Tagging
words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

# Named entity recognition
namedEnt = nltk.ne_chunk(tagged_words)
namedEnt.draw()

"""
ORGANIZATION	Georgia-Pacific Corp., WHO
PERSON	Eddy Bonte, President Obama
LOCATION	Murray River, Mount Everest
DATE	June, 2008-06-29
TIME	two fifty a m, 1:30 p.m.
MONEY	175 million Canadian Dollars, GBP 10.40
PERCENT	twenty pct, 18.75 %
FACILITY	Washington Monument, Stonehenge
GPE	South East Asia, Midlothian
"""