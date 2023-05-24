from VHealth import app
from flask import Flask, render_template, request, jsonify
from VHealth.Text_Predict import Text_classification_predict
from VHealth.Text_Predict.Text_classification_predict import TextClassificationPredict
from VHealth.Text_Predict.Text_classification_predict import TextClassificationPredict
from VHealth.model.LDA import make_texts_corpus
from VHealth.model.SVM import SVM_Model
from VHealth.model.distances import get_most_similar_documents
from VHealth.common import File
from gensim.models.ldamodel import LdaModel
from gensim.test.utils import datapath
from googletrans import Translator
from flask_wtf import FlaskForm

import numpy as np
import pandas as pd
import os
import gensim  # noqa
import joblib  # noqa
import VHealth.common.Settings


def get_parentDir():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    return parentDir


def load_model():
    # load LDA model
    lda_model = gensim.models.ldamodel.LdaModel.load(
        VHealth.common.Settings.PATH_LDA_MODEL
    )
    # load corpus
    corpus = gensim.corpora.MmCorpus(
        VHealth.common.Settings.PATH_CORPUS
    )
    # load dictionary
    id2word = gensim.corpora.Dictionary.load(
        VHealth.common.Settings.PATH_DICTIONARY
    )
    # load documents topic distribution matrix
    doc_topic_dist = joblib.load(
        VHealth.common.Settings.PATH_DOC_TOPIC_DIST
    )
    # doc_topic_dist = np.array([np.array(dist) for dist in doc_topic_dist])

    return lda_model, corpus, id2word, doc_topic_dist


lda_model, corpus, id2word, doc_topic_dist = load_model()


def show_post(content):
    df = pd.read_csv('C:\\Users\ADMIN\PycharmProjects\ModelQA_NCKH\VHealth\data\CSV\Exercises_EN.csv')
    # content =request.form.get('question_test')
    # preprocessing
    text_corpus = make_texts_corpus([content])
    bow = id2word.doc2bow(next(text_corpus))
    # print(bow)
    doc_distribution = np.array(
        [doc_top[1] for doc_top in lda_model.get_document_topics(bow=bow)]
    )
    # recommender posts
    most_sim_ids = list(get_most_similar_documents(
        doc_distribution, doc_topic_dist))[1:]
    # print(most_sim_ids)
    most_sim_ids = [int(id_) for id_ in most_sim_ids]

    posts = df.loc[most_sim_ids, ['Title', 'Link', 'Original_Title']]

    for index, row in posts.iterrows():
        response = "Title:" + row["Original_Title"] + "- Link:" + row["Link"]
    return response


def get_chat(message):
    tcp = TextClassificationPredict(message, File.get_dbtrain(), File.get_dbtrain_extend(), File.get_dbanswers())
    result = tcp.Text_Predict()
    response = {"message": result}
    # response="TEXT"
    return response
# class NumerologyForm(FlaskForm):

