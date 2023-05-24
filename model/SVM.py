
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.svm import SVC
from VHealth.Transformer.Feature_transformer import FeatureTransformer
class SVM_Model(object):
    def __init__(self):
        self.clf = self._init_pipeline()

    @staticmethod
    def _init_pipeline():
        pipe_line = Pipeline([
            ("transformer", FeatureTransformer()),
            ("vect", CountVectorizer()),
            ("tfidf", TfidfTransformer()),
            ("clf", SVC(kernel='linear', C=1, gamma=10.0, probability=True))
        ])

        return pipe_line
# X = ["This is a sample document.", "Another document to test.", "Yet another document."]
# y = [0, 1, 0]
# import pandas as pd
# X_series = pd.Series(X)
#
# svm_model = SVM_Model()
# svm_model.clf.fit(X_series, y)
