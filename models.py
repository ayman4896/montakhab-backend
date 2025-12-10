from sqlalchemy import Column, Integer, String
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    age = Column(String, nullable=True)
    weight = Column(String, nullable=True)

    organization = Column(String, nullable=True)   # الجهة / الهيئة
    nationalID = Column(String, nullable=True)     # الرقم القومي

    phone = Column(String, nullable=True)
    category = Column(String, nullable=False)      # الناشئين، الشباب، الأوليمبي

    photo = Column(String, nullable=True)          # Base64
