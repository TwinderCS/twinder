import pytest
from text_analysis.text_analysis import get_opinion_rate

@pytest.mark.parametrize("positive_opinions", [
    #"It was amazing !",    -> 2
    #"I appreciate that",   -> 2
    #"thank you so much"    -> 2
])

def test_positive_opinion_rate(positive_opinions):
    rate = get_opinion_rate(positive_opinions)
    assert rate.index(max(rate)) == 0

@pytest.mark.parametrize("neutral_opinions", [
    #"i am hungry",             -> 2
    #"the sky is blue today",   -> 2
    #"my name is Shadock"       -> 2
])

def test_neutral_opinion_rate(neutral_opinions):
    rate = get_opinion_rate(neutral_opinions)
    assert rate.index(max(rate)) == 1

@pytest.mark.parametrize("negative_opinions", [
    "LoL is so toxic !",
    "modern art is soooooo great",
    "the deutsch class is boring"
])

def test_negative_opinion_rate(negative_opinions):
    rate = get_opinion_rate(negative_opinions)
    assert rate.index(max(rate)) == 2
