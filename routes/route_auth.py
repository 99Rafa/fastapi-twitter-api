from fastapi import APIRouter, status

from models.user import User

router = APIRouter()


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new User",
)
def signup():
    """
    Signup

    Registers a user in the app

    Parameters:
        Request body:
            - user: UserRegister

    Returns:
        User
    """


@router.post(
    path="/login",
    response_model=User,
    summary="Login a User",
)
def login():
    pass
