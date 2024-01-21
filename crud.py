from sqlalchemy.orm import Session

from models import *


def get_menu(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()
