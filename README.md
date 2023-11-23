# Project of the coding weeks 2020-2021 of the Twinder® Team

## Description

Create a programm that propose some Twitter profiles to the user from its tweets.
**add infos**

## The Twinder® Team
**add work distribution**

- Anas Lecaillon (Maitre de l'Univers (Entre autres))
- Mohamed Koucha (Être humain (Je suppose))
- Balthazar (TextBlob classifier implementation for polarity (pos, neu, neg), training of the classifier, 
            combination of the classifier, the emotion model and the topic model to create each user's metric,
            calculating closest users, and a little of dataframe cleaning, and create the metric dataframe)
- Sarah
- Léna (Tests and global problems, create the metric dataframe)

## Dependencies
- `torch`
- `torchtext`
- `nltk`
- `dash`
- `spacy`
- `autocorrect`
- `wandb`
- `pytorch_lightning`
- `numpy`
- `pandas`
- `sys`


## To Execute       
**explain how to run the project (git clone then what ?)**
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
│       ├── login.py
│       └── metrics.py
├── assets
│   ├── fond-degrade-saint-valentin_23-2149242406.avif
│   ├── newsarahcss.css
│   ├── sarahdesign.png
│   └── sarahwallpaper.png
├── coverage_reports
├── coverage_reports_metrics_handlers
├── coverage_reports_text_analysis
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
│   ├── tweets.py
│   └── users.py
├── designsarah.css
├── dumps
│   ├── check_topic.py
│   ├── df.pkl
│   ├── emotion.csv
│   ├── emotion_lemmatized.pkl
│   ├── emotion_model.ckpt
│   ├── emotion.pkl
│   ├── emotion.vocab
│   ├── font.ttf
│   ├── metrics.csv
│   ├── metrics.pkl
│   ├── tinder_logo.png
│   ├── topic.csv
│   ├── topic_model.ckpt
│   ├── topic.pkl
│   ├── topic.vocab
│   ├── tweet_emotions.csv
│   ├── tweets.csv
│   ├── tweets.pkl
│   └── twitter_logo.png
├── images
│   ├── twinder100.png
│   ├── twinder1024.png
│   ├── twinder8192.png
│   └── twinder.svg
├── improved-sarah-interface.py
├── metrics_handlers
│   ├── metrics.py
│   └── models.py
├── model_notebooks
│   └── emotion.ipynb
├── README.md
├── tests
│   └── test_classifier.py
│   └── test_emotion_classifer.py
│   └── test_metrics.py
│   ├── test_text_analysis.py
│   ├── test_topic_classifier.py
│   └── test_with_pytest.py
├── text_analysis
│   ├── classifier.py
│   ├── cl_data.obj
│   └── emotion_classifier.py
│   └── text_analysis.py
│   └── topic_classifier.py
├── textblob
│   └── blob.py
├── tweet_collection
│   ├── collection.py
│   ├── credentials.py
│   ├── tweet_collection.py
│   └── twitter_connection.py
├── tweet_visualization
│   ├── seaborn_own.py
│   └── tweet_visualization.py
└── wordcloud
    ├── __init__.py
    └── wc.py
```

## Informations about tests

## MVC

## What else could we have done if the Coding Weeks were longer ?

- Limitations of the database : geolocalisation, if all users are active (date of the last tweet)
- Work on the classifier models
- Limitations of the API, instead add an implementation fonctionnality : an user can upload its tweets and get the compatibility with all the users in the database and is added to the database
- adaptive metric depending on the choice previously made by the user
- if the following system is taken into account, add it to the metric system
