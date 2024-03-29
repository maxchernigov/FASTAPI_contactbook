from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import UserLogin
from src.schemas import LoginModel


async def get_user_by_email(email: str, db: Session) -> UserLogin:
    return db.query(UserLogin).filter(UserLogin.email == email).first()


async def create_user(body: LoginModel, db: Session) -> UserLogin:
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = UserLogin(**body.model_dump(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)    
    return new_user


async def update_token(user: UserLogin, token: str | None, db: Session) -> None:
    user.refresh_token = token
    db.commit()