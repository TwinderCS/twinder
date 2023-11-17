# Project of the coding weeks 2020-2021 of the Twinder® Team

## Description

Create a programm that propose some Twitter profiles to the user from its tweets.


## The Twinder® Team

- Anas Lecaillon (Maitre de l'Univers (Entre autres))
- Mohamed Koucha (Être humain (Je suppose))
- Balthazar
- Sarah
- Léna

## Dependencies
- `torch`
- `torchtext`
- `nltk`
- `dash`
- `spacy`
- `autocorrect`
- `wandb`
- `pytorch_lightning`

## To Execute
```bash
python3 -m spacy download en
```

## Current Project Structure
```
├── 1er_essai_interface_sarah.py
├── app
│   ├── app.py
│   └── pages
│       ├── feed.py
│       ├── index.py
│       └── login.py
├── dash
│   ├── app_objects.py
│   ├── app.py
│   ├── demand.py
│   ├── Input_interface.py
│   ├── main_page.py
│   ├── request.py
│   └── update_candidate.py
├── data_handling
│   ├── create_dataframe.py
│   ├── __init__.py
│   ├── tweets.py
│   └── users.py
├── dumps
│   ├── check_topic.py
│   ├── df.pkl
│   ├── emotion.csv
│   ├── emotion_lemmatized.pkl
│   ├── emotion.pkl
│   ├── font.ttf
│   ├── metrics.pkl
│   ├── tinder_logo.png
│   ├── topic.csv
│   ├── tweet_emotions.csv
│   ├── tweets.csv
│   ├── tweets.pkl
│   └── twitter_logo.png
├── images
│   ├── twinder100.png
│   ├── twinder1024.png
│   ├── twinder8192.png
│   └── twinder.svg
├── __init__.py
├── metrics_handlers
│   ├── __init__.py
│   ├── metrics.py
│   └── models.py
├── metrics.py
├── model_notebooks
│   └── emotion.ipynb
├── README.md
├── tests
│   ├── __init__.py
│   ├── test_text_analysis.py
│   └── test_with_pytest.py
├── text_analysis
│   ├── classifier_data.py
│   ├── classifier.py
│   ├── cl_data.obj
│   ├── emotion_classifier.py
│   ├── __init__.py
│   ├── text_analysis.py
│   └── topic_classifier.py
├── textblob
│   └── blob.py
├── tweet_collection
│   ├── collection.py
│   ├── credentials.py
│   ├── __init__.py
│   ├── tweet_collection.py
│   └── twitter_connection.py
├── tweet_visualization
│   ├── seaborn_own.py
│   └── tweet_visualization.py
└── wordcloud
    ├── __init__.py
    └── wc.py
```
