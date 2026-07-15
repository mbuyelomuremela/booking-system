from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.database.database import Base
#from app.models.bookings import Bookings

class Users(Base):
    __tablename__ = "users"
    
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    cellphone_number = Column(String(15), nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, index=True)

    bookings = relationship("Bookings", back_populates="owner")
