import json
from datetime import datetime
from typing import List

from fastapi import APIRouter, Body, status

from db.mongo_connection import MongoDB
from models.tweet import Tweet

router = APIRouter()


@router.get(
    path="",
    response_model=List[Tweet],
    summary="Shows all tweets",
)
def show_tweets():
    """
    Show all tweets

    Returns:
    - All tweets in the app
    """
    db = MongoDB.get_instance()
    tweets_collection = db.tweets

    tweets = tweets_collection.find()

    return list(tweets)


@router.post(
    path="",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Creates a new tweet",
)
def create_tweet(tweet: Tweet = Body(...)):
    """
    Create tweet

    Creates a new tweet in the database

    Parameters:
    - Request body:
        - tweet: Tweet

    Returns:
    - Tweet
    """

    db = MongoDB.get_instance()
    tweets_collection = db.tweets

    tweet_dict = tweet.dict()
    tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
    tweet_dict["created_at"] = str(datetime.now())
    tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

    tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
    tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])

    tweets_collection.insert_one(tweet_dict)

    return tweet_dict


@router.get(
    path="/{tweet_id}",
    response_model=Tweet,
    summary="Gets a tweet based on the id",
)
def show_tweet():
    pass


@router.delete(
    path="/{tweet_id}",
    response_model=Tweet,
    summary="Deletes a tweet based on the id",
)
def delete_tweet():
    pass


@router.put(
    path="/{tweet_id}",
    response_model=Tweet,
    summary="Updates a tweet based on the id",
)
def delete_tweet():
    pass
