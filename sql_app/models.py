import uuid

from sqlalchemy import Column, Integer, String
import sys, os
sys.path.append(os.path.abspath('.'))

from sql_app.database import Base

class Note(Base):
    __tablename__ = "notas"
    #id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4())) mysql
    id = Column(String, primary_key=True, index=True,default=lambda: str(uuid.uuid4()))
    text = Column(String, nullable=True, default="new")
    title = Column(String, nullable=True, default="new")


