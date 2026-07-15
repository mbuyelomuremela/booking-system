from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.models .service import Services
from app.models.user import Users

class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    booking_date = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default="pending")

    service = relationship("Services", back_populates="bookings")
    owner = relationship("Users", back_populates="bookings")