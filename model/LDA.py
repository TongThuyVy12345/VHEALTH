import pandas as pd
import gensim
import itertools
import joblib
import logging
import numpy as np
from gensim.utils import simple_preprocess
from gensim import corpora, models
from VHealth.model.distances import get_most_similar_documents

import os
PATH_CORPUS = '/model/corpus.mm'
PATH_DICTIONARY = '/model/dictionary.dict'
PATH_LDA_MODEL = '/model/lda_model.model'
PATH_DOC_TOPIC_DIST = "/model/doc_topic_dist.dat"
def get_parentDir():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    return parentDir
df = get_parentDir() + '\data\CSV\FExercises_EN.csv'


def head(stream, n=10):
    """
    Return the first `n` elements of the stream, as plain list.
    """
    return list(itertools.islice(stream, n))


def tokenize(text, STOPWORDS):
    # deacc=True to remove punctuations
    return [token for token in simple_preprocess(text, deacc=True)
            if token not in STOPWORDS]


def make_texts_corpus(sentences):
    for sentence in sentences:
        yield simple_preprocess(sentence, deacc=True)


class StreamCorpus(object):
    def __init__(self, sentences, dictionary, clip_docs=None):
        """
        Parse the first `clip_docs` documents
        Yield each document in turn, as a list of tokens.
        """
        self.sentences = sentences
        self.dictionary = dictionary
        self.clip_docs = clip_docs

    def __iter__(self):
        for tokens in itertools.islice(make_texts_corpus(self.sentences),
                                       self.clip_docs):
            yield self.dictionary.doc2bow(tokens)

    def __len__(self):
        return self.clip_docs


class LDAModel:

    def __init__(self, num_topics, passes, chunksize,
                 random_state=100, update_every=1, alpha='auto',
                 per_word_topics=False):
        """
        :param sentences: list or iterable (recommend)
        """

        # data
        self.sentences = None

        # params
        self.lda_model = None
        self.dictionary = None
        self.corpus = None

        # hyperparams
        self.num_topics = num_topics
        self.passes = passes
        self.chunksize = chunksize
        self.random_state = random_state
        self.update_every = update_every
        self.alpha = alpha
        self.per_word_topics = per_word_topics

        # init model
        # self._make_dictionary()
        # self._make_corpus_bow()

    def _make_corpus_bow(self, sentences):
        self.corpus = StreamCorpus(sentences, self.id2word)
        # save corpus
        gensim.corpora.MmCorpus.serialize(PATH_CORPUS, self.corpus)

    def _make_corpus_tfidf(self):
        pass

    def _make_dictionary(self, sentences):
        self.texts_corpus = make_texts_corpus(sentences)
        self.id2word = gensim.corpora.Dictionary(self.texts_corpus)
        self.id2word.filter_extremes(no_below=10, no_above=0.25)
        self.id2word.compactify()
        self.id2word.save(PATH_DICTIONARY)

    def documents_topic_distribution(self):
        doc_topic_dist = np.array(
            [[tup[1] for tup in lst] for lst in self.lda_model[self.corpus]]
        )
        # save documents-topics matrix
        joblib.dump(doc_topic_dist, PATH_DOC_TOPIC_DIST)
        return doc_topic_dist

    def fit(self, sentences):
        from itertools import tee
        sentences_1, sentences_2 = tee(sentences)
        self._make_dictionary(sentences_1)
        self._make_corpus_bow(sentences_2)
        self.lda_model = gensim.models.ldamodel.LdaModel(
            self.corpus, id2word=self.id2word, num_topics=64, passes=5,
            chunksize=100, random_state=42, alpha=1e-2, eta=0.5e-2,
            minimum_probability=0.0, per_word_topics=False
        )
        self.lda_model.save(PATH_LDA_MODEL)

    def transform(self, sentence):
        """
        :param document: preprocessed document
        """
        document_corpus = next(make_texts_corpus([sentence]))
        corpus = self.id2word.doc2bow(document_corpus)
        document_dist = np.array(
            [tup[1] for tup in self.lda_model.get_document_topics(bow=corpus)]
        )
        return corpus, document_dist

    def predict(self, document_dist):
        doc_topic_dist = self.documents_topic_distribution()
        return get_most_similar_documents(document_dist, doc_topic_dist)


    def compute_coherence_values(self, mallet_path, dictionary, corpus,
                                 texts, end=40, start=2, step=3):
        """
        Compute c_v coherence for various number of topics
        Parameters:
        ----------
        dictionary : Gensim dictionary
        corpus : Gensim corpus
        texts : List of input texts
        end : Max num of topics
        Returns:
        -------
        model_list : List of LDA topic models
        coherence_values : Coherence values corresponding to the LDA model
                           with respective number of topics
        """
        coherence_values = []
        model_list = []
        for num_topics in range(start, end, step):
            model = gensim.models.wrappers.LdaMallet(
                mallet_path, corpus=self.corpus,
                num_topics=self.num_topics, id2word=self.id2word)
            model_list.append(model)
            coherencemodel = gensim.models.coherencemodel.CoherenceModel(
                model=model, texts=self.texts_corpus,
                dictionary=self.dictionary, coherence='c_v'
            )
            coherence_values.append(coherencemodel.get_coherence())

        return model_list, coherence_values

    def print_topics(self):
        pass
