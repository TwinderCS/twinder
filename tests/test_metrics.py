import pytest
import numpy as np
import sys
sys.path.append("metrics_handlers")
from metrics import topic_to_vector, get_metric_from_tweet, get_metric_from_user, distance, get_closest_users

@pytest.fixture
def sample_tweet():
    return "Sample tweet text."

@pytest.fixture
def sample_user():
    return "sample_user"

def test_topic_to_vector():
    topic_vector = topic_to_vector("politics")
    assert isinstance(topic_vector, np.ndarray)
    assert len(topic_vector) == 6  # Assuming there are 6 topics

def test_get_metric_from_tweet(sample_tweet):
    metrics = get_metric_from_tweet(sample_tweet)
    assert isinstance(metrics, np.ndarray)
    assert len(metrics) == 14  # Assuming the size of the resulting vector is 14

def test_get_metric_from_user(sample_user):
    metrics = get_metric_from_user(sample_user)
    assert isinstance(metrics, np.ndarray)
    assert len(metrics) == 14  # Assuming the size of the resulting vector is 14

def test_distance():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    dist = distance(v1, v2)
    assert dist == pytest.approx(5.196, rel=1e-3)  # Approximate value

def test_get_closest_users(sample_user):
    closest_users = get_closest_users(sample_user, n=5, N=10)
    assert isinstance(closest_users, np.ndarray)
    assert len(closest_users) == 5

"""
The error you're encountering, "IndexError: single positional indexer is out-of-bounds," typically occurs when you're trying to access an element in a Pandas DataFrame using an index that doesn't exist.

In your case, it seems to be happening when you're trying to access the metric of the specified username in your get_closest_users function. Let's check the relevant part of your code:

python

metric = df_metric[df_metric['username'] == username]['metric'].iloc[0]

This line is trying to filter the DataFrame based on the 'username' column and then access the 'metric' column of the resulting DataFrame. The error suggests that there might be an issue with this operation, possibly because the DataFrame is empty or the specified index is out of bounds.

Here are a few things you can check:

    Make sure the DataFrame is not empty:
    Before trying to access the metric, check if the filtered DataFrame is not empty. You can add a print statement to debug:

    python

print(df_metric[df_metric['username'] == username])
metric = df_metric[df_metric['username'] == username]['metric'].iloc[0]

If this DataFrame is empty, it means that there is no user with the specified username in your DataFrame.

Check if the username exists in the DataFrame:
Ensure that the specified username (sample_user in this case) actually exists in your DataFrame. You might want to print the unique usernames in your DataFrame:

python

print(df_metric['username'].unique())

Make sure that 'sample_user' is present in this list.

Handle the case where the DataFrame is empty:
If it's possible that the DataFrame might be empty for some usernames, you should handle this case to avoid index out-of-bounds errors. You can modify your code like this:

python

    filtered_df = df_metric[df_metric['username'] == username]
    if not filtered_df.empty:
        metric = filtered_df['metric'].iloc[0]
    else:
        # Handle the case where the DataFrame is empty for the specified username
        metric = None  # Or any other appropriate value

    This ensures that you only try to access the metric if the DataFrame is not empty.

By addressing these points, you should be able to identify and fix the issue causing the index out-of-bounds error.
"""