from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.orm import relationship

from app.database.database import Base
#from app.models.bookings import Bookings

class Services(Base):
    __tablename__ = "services"

    name = Column(String(250), nullable=False, index=True)
    description = Column(String(1000), nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    id = Column(Integer, primary_key=True, index=True)

    bookings = relationship("Bookings", back_populates="service")