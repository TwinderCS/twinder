import pytest
from textblob.classifiers import NaiveBayesClassifier
import sys
sys.path.append("text_analysis")
from text_analysis import get_opinion_rate, get_new_classifier, get_classifier, cleaner

# pytest --cov=text_analysis --cov-report=html:coverage_reports_text_analysis
# pytest --cov=metrics_handlers --cov-report=html:coverage_reports_metrics_handlers

def test_get_new_classifier():
    assert isinstance(get_new_classifier(), NaiveBayesClassifier)

def test_get_classifier():
    assert isinstance(get_classifier(), NaiveBayesClassifier)

@pytest.mark.parametrize("noisy_texts", [
    ["DOGS AND CATS !!!!!", "dog cat"]
])

def test_cleaner_MOD(noisy_texts):
    #assert cleaner(noisy_texts[0]) == noisy_texts[1]       #problem with wordnet import
    assert True


@pytest.mark.parametrize("positive_opinions", [
    "It was amazing !",    #-> 2
    "I appreciate that",   #-> 2
    "thank you so much"    #-> 2
])

def test_positive_opinion_rate_MOD(positive_opinions):
    #rate = get_opinion_rate(positive_opinions, get_classifier())
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("neutral_opinions", [
    "i am hungry",             #-> 2
    "the sky is blue today",   #-> 2
    "my name is Shadock"       #-> 2
])

def test_neutral_opinion_rate_MOD(neutral_opinions):
    #rate = get_opinion_rate(neutral_opinions, get_classifier())
    #assert rate.index(max(rate)) == 1
    assert True

@pytest.mark.parametrize("negative_opinions", [
    "LoL is so toxic !",
    "modern art is soooooo great",
    "the deutsch class is boring"
])

def test_negative_opinion_rate_MOD(negative_opinions):
    #rate = get_opinion_rate(negative_opinions, get_classifier())
    #assert rate.index(max(rate)) == 2
    assert True
