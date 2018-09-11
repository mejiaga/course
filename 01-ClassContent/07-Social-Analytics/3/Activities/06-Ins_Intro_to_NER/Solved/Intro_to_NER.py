import spacy
from spacy import displacy
from IPython.core.display import display, HTML

# Load spaCy model
nlp = spacy.load('en_core_web_md')

# Save a sentence for processing
doc = nlp(u"Amazon is already hiring near the nation's capital — and Boston.")

# Print the entity text, starting char, ending char, and label
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label)

# What is `GPE`, anyway?
spacy.explain('GPE')

# Create an entity visualization from a news article
# Save an excerpt from a news article
news_article = """Amazon (AMZN) is considered to be one of the greatest growth
stocks of our generation. After a mixed but overall positive Prime Day, AMZN
reached an all time high price of $1860, reflecting a market capitalization
greater than $900 billion, which would make it the second most valuable company
in the world after Apple (NASDAQ:AAPL)."""

# Ready the article for processing
doc2 = nlp(news_article)

# Add a title to the document
doc2.user_data['title'] = 'News Snippet'

# Render the visualization.
# Note the syntax differences between a python file and a notebook file
html = displacy.serve(doc2, style='ent')
display(HTML(html))
