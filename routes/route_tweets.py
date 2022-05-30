import uuid
from datetime import datetime
from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, status
from pymongo import ReturnDocument

from db.mongo_connection import MongoDB
from models.tweet import Tweet, TweetInfo

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
def create_tweet(tweet: TweetInfo = Body(...)):
    """
    Create tweet

    Creates a new tweet in the database

    Parameters:
    - Request body:
        - tweet: TweetInfo

    Returns:
    - Tweet
    """

    db = MongoDB.get_instance()
    tweets_collection = db.tweets

    tweet_dict = tweet.dict()
    tweet_dict["tweet_id"] = str(uuid.uuid4())
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
def show_tweet(tweet_id: str = Path(...)):
    """
    Get tweet based on a given id

    Parameters:
    - Path:
        - tweet_id: UUID

    Returns:
    - Tweet
    """

    db = MongoDB.get_instance()
    tweets_collection = db.tweets

    tweet_doc = tweets_collection.find_one({"tweet_id": tweet_id})

    if not tweet_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found",
        )

    return dict(tweet_doc)


@router.delete(
    path="/{tweet_id}",
    response_model=Tweet,
    summary="Deletes a tweet based on the id",
)
def delete_tweet(tweet_id: str = Path(...)):
    """
    Delete a tweet

    Parameters:
    - Path:
        - tweet_id: UUID

    Returns:
    - Tweet
    """

    db = MongoDB.get_instance()
    tweets_collection = db.tweets

    tweet_doc = tweets_collection.find_one_and_delete({"tweet_id": tweet_id})

    if not tweet_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found",
        )

    return tweet_doc


@router.put(
    path="/{tweet_id}",
    response_model=Tweet,
    summary="Updates a tweet based on the id",
)
def update_tweet(
    tweet_id: str = Path(...),
    content: str = Body(
        ...,
        min_length=1,
        max_length=256,
    ),
):
    """
    Update tweet

    Parameters:
    - Path:
        - tweet_id: UUID
    - Request body:
        - content: str

    Returns:
    - Tweet
    """

    db = MongoDB.get_instance()
    tweets_collection = db.tweets

    tweet_doc = tweets_collection.find_one_and_update(
        filter={"tweet_id": tweet_id},
        update={
            "$set": {
                "content": content,
                "updated_at": str(datetime.now()),
            },
        },
        return_document=ReturnDocument.AFTER,
    )

    if not tweet_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found",
        )

    return tweet_doc
