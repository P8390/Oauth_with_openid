from sqlalchemy import Column, DateTime, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base
from database import session


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    profile_pic = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    is_deleted = Column(Integer, server_default=text("'0'"))
    unique_id = Column(String(100), nullable=False, unique=True)

    @staticmethod
    def get_user_info(unique_id):
        user_obj = session.query(User).filter(User.unique_id == unique_id).first()
        if not user_obj:
            print('user object does not exist')
            # raise ValueError('USER-OBJECT-DOES-NOT-FOUND')
        return user_obj

    @staticmethod
    def create_new_user(**kwargs):
        user_obj = User(**kwargs)
        session.add(user_obj)
        session.flush()
        return user_obj
