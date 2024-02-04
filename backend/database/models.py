from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy_utils import URLType

from .config import Base


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    slug = Column(String, nullable=True)
    name = Column(String)
    original_url = Column(URLType)
    fake_url = Column(URLType)
