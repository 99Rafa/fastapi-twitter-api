from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from models.user import User


class BaseTweet(BaseModel):
    tweet_id: UUID = Field(...)


class TweetInfo(BaseModel):
    content: str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(None)
    by: User = Field(...)


class Tweet(BaseTweet, TweetInfo):
    pass
