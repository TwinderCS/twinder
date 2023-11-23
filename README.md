# Project of the coding weeks 2020-2021 of the Twinder® Team

## GitLab and pwpt

https://docs.google.com/presentation/d/1eBpYBZ3qCNge3yiuCJ5f1ER0wrEK_rBEQPP6JIsN4SA/edit#slide=id.gc6f9e470d_0_0

https://gitlab-cw4.centralesupelec.fr/twittos/twittos-s1/

## Description

Create a programm that propose some Twitter profiles to the user from its tweets.


## The Twinder® Team

- Anas Lecaillon
- Mohamed Koucha
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
- `numpy`
- `pandas`
- `sys`
- `ssl`
- `time`

# To run the first time and to execute

Run the config.py file and download the packages

```bash
python3 -m spacy download en
```

# To run the project

Execute the app/app.py file

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
│   ├── test_emotion_classifier.py
│   ├── test_text_analysis.py
│   ├── test_topic_classifier.py
│   └── test_with_pytest.py
├── text_analysis
│   ├── classifier.py
│   ├── cl_data.obj
│   ├── emotion_classifier.py
│   ├── text_analysis.py
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
