# import gensim
import pandas as pd
from gensim import corpora, models

df = pd.read_csv('D:/Data AI/Exercises_EN.csv')
import spacy

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
import gensim
from gensim.utils import simple_preprocess
from gensim.corpora import Dictionary
documents = list(df['Title'].values)
tokens = [simple_preprocess(doc) for doc in documents]
dictionary = Dictionary(tokens)
doc_clean = df["Title"].apply(lambda x: simple_preprocess(x))
corpus = [dictionary.doc2bow(doc) for doc in doc_clean]
# Train the LDA model
import gensim

num_topics = 10  # Set the number of topics
lda_model = gensim.models.LdaModel(corpus, num_topics=64, id2word=dictionary, passes=5, chunksize=100, random_state=42,
                                   alpha=1e-2, eta=0.5e-2, minimum_probability=0.0, per_word_topics=True)
lda_model.save( 'LDA.model')
