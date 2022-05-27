from typing import List

from fastapi import APIRouter

from models.user import User

router = APIRouter()


@router.get(
    path="",
    response_model=List[User],
    summary="Shows all registered users",
)
def show_all_users():
    pass


@router.get(
    path="/{user_id}",
    response_model=User,
    summary="Shows a user based on the id",
)
def show_user():
    pass


@router.delete(
    path="/{user_id}",
    response_model=User,
    summary="Deletes a user based on the id",
)
def delete_user():
    pass


@router.put(
    path="/{user_id}",
    response_model=User,
    summary="Updates a user based on the id",
)
def update_user():
    pass
