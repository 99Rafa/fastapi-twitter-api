from typing import List

from fastapi import APIRouter, status

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
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Creates a new tweet",
)
def create_tweet():
    pass


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
