import json
from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, status
from pymongo import ReturnDocument

from db.mongo_connection import MongoDB
from models.user import User, UserUpdate

router = APIRouter()


@router.get(
    path="",
    response_model=List[User],
    summary="Shows all registered users",
)
def show_all_users():
    """
    Show all users

    Shows all registered users

    Returns;
    - List with all users in the app
    """

    db = MongoDB.get_instance()
    users_collection = db.users

    users = users_collection.find()

    return list(users)


@router.get(
    path="/{user_id}",
    response_model=User,
    summary="Shows a user based on the id",
)
def show_user(user_id: str = Path(...)):
    """
    Get a user based on a given id

    Parameters:
    - Path:
        - user_id: UUID

    Returns:
    - User
    """

    db = MongoDB.get_instance()
    users_collection = db.users

    user_doc = users_collection.find_one({"user_id": user_id})

    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user_doc


@router.delete(
    path="/{user_id}",
    response_model=User,
    summary="Deletes a user based on the id",
)
def delete_user(user_id: str = Path(...)):
    """
    Delete a user based on a given id

    Parameters:
    - Path:
        - user_id: UUID

    Returns:
    - User
    """
    db = MongoDB.get_instance()
    users_collection = db.users

    user_doc = users_collection.find_one_and_delete({"user_id": user_id})

    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user_doc


@router.put(
    path="/{user_id}",
    response_model=User,
    summary="Updates a user based on the id",
)
def update_user(
    user_id: str = Path(...),
    user_info: UserUpdate = Body(...),
):
    """
    Update user

    Parameters:
    - Path:
        - user_id: UUID
    - Request body:
        - user_info: UserUpdate

    Returns:
    - User
    """

    db = MongoDB.get_instance()
    users_collection = db.users

    user_doc = users_collection.find_one_and_update(
        filter={"user_id": user_id},
        update={
            "$set": {
                "first_name": user_info.first_name,
                "last_name": user_info.last_name,
                "birth_date": user_info.birth_date,
                "email": user_info.email,
            },
        },
        return_document=ReturnDocument.AFTER,
    )

    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user_doc
