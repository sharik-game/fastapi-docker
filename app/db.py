# app/db.py

import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):

    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    hashed_password: str = ormar.String(max_length=128,
                                        unique=True,
                                        nullable=False)
    price: int = ormar.Integer(default=0, nullable=True)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)