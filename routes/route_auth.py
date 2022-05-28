import json

from fastapi import APIRouter, Body, status

from models.user import User, UserRegister

router = APIRouter()


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new User",
)
def signup(user: UserRegister = Body(...)):
    """
    Signup

    Registers a user in the app

    Parameters:
    - Request body:
        - user: UserRegister

    Returns:
    - User
    """
    with open("databases/users.json", "r+", encoding="utf-8") as f:
        result = json.load(f)

        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])

        result.append(user_dict)
        f.seek(0)
        json.dump(result, f)

        return user_dict


@router.post(
    path="/login",
    response_model=User,
    summary="Login a User",
)
def login():
    pass
