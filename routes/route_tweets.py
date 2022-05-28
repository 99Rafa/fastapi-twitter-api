import json
from datetime import datetime
from typing import List

from fastapi import APIRouter, Body, status

from models.tweet import Tweet

router = APIRouter()


@router.get(
    path="",
    response_model=List[Tweet],
    summary="Shows all tweets",
)
def show_tweets():
    pass


@router.post(
    path="",
    # response_model=Tweet,
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
    with open("databases/tweets.json", "r+", encoding="utf-8") as f:
        result = json.load(f)

        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(datetime.now())
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])

        result.append(tweet_dict)
        f.seek(0)
        json.dump(result, f)

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
