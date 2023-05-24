from nltk.tokenize import word_tokenize
from nltk import pos_tag
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, *_):
        return self

    def transform(self, X, y=None, **fit_params):
        result = X.apply(lambda text: " ".join([word[0] + "_" + word[1] for word in pos_tag(word_tokenize(text))]))
        return result
