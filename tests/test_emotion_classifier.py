import pytest

"""
from model_modulee import MyModel

load trained model
model = MyModel.load_from_checkpoint('path_to_checkopoint.ckpt)

preprocess the phrase

convert to tensor

input_tensor = torch.tensor(processed_phrase).unsqueeze(0)

"""
@pytest.mark.parametrize("positive_tweets", [
    "Life is so great !"
])

def test_positive_opinion_rate(positive_tweets):
    #rate = get_opinion_rate(positive_opinions)
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("sad_tweets", [
    "After 200+ hours of work, my projet didn't get selected, without any explanation. Man, I don't feel great!"
])

def test_sad_tweets(sad_tweets):
    #rate = get_opinion_rate(sad_tweets)
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("funny_tweets", [
    "Happy birthday Mom ! I wish the best for you"
])

def test_funny_tweets(funny_tweets):
    #rate = get_opinion_rate(sad_tweets)
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("neutral_tweets", [
    "The sky is blue today, it's a color"
])

def test_neutral_tweets(neutral_tweets):
    #rate = get_opinion_rate(sad_tweets)
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("anxious_tweets", [
    "I just got a 3 for my philosophy test, don't know how to annonce that to my parents..."
])

def test_anxious_tweets(anxious_tweets):
    #rate = get_opinion_rate(sad_tweets)
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("surprised_tweets", [
    "My boyfriend just got us a kitten ! I didn't expexted this at all, and now i have to find a beautiful name for this cutie !"
])

def test_surprised_tweets(surprised_tweets):
    #rate = get_opinion_rate(sad_tweets)
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("joyful_tweets", [
    "I just landed ! Can't wait to explore Paris and get to taste some croissants :)"
])

def test_joyful_tweets(joyful_tweets):
    #rate = get_opinion_rate(sad_tweets)
    #assert rate.index(max(rate)) == 0
    assert True

@pytest.mark.parametrize("hateful_tweets", [
    "How dare you ! Don't worry, you will get what you deserve before Christmas... "
])

def test_hateful_tweets(hateful_tweets):
    #rate = get_opinion_rate(sad_tweets)
    #assert rate.index(max(rate)) == 0
    assert True


#negation
#robustness to noise (pronum, surname, time conjugaison)


@pytest.mark.parametrize("negation_tweets", [
   ["I haven't failed this test, my parents are going to be happy !", "I failed this test, my parents aren't going to be happy !"]
])

def test_negation(negation_tweets):
    #negation_tweets[0] != negation_tweets[1]
    assert True


@pytest.mark.parametrize("noised_tweets", [
    ["I just come from a shopping session with Sarah, she was so funny", "I just come from a shopping session with William, he was so funny"]
])

def test_noised(noised_tweets):
    #noised_tweets[0] != noised_tweets[1]
    assert True