from api.db.database import Base
from sqlalchemy import Column, Boolean, String, Integer, DateTime
from datetime import datetime



class User(Base):
    __tablename__="xin_employees"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=False)
    password = Column(String(300), nullable=False)
    apikey =  Column(String(300), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class Company(Base):
    __tablename__="xin_companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    trading_name = Column(String(100), unique=True, index=True, nullable=False)
    registration_no = Column(String(100),  nullable=True)
    government_tax = Column(Boolean, default=True)
    email = Column(String(300), nullable=True)
    logo =  Column(String(300), nullable=True)
    contact_number = Column(String(100),  nullable=True)
    website_url = Column(String(100),  nullable=True)
    address_1 = Column(Boolean, default=True)
    city = Column(String(300), nullable=True)
    state =  Column(String(300), nullable=True)
    zipcode = Column(String(100),  nullable=True)
    country = Column(String(100),  nullable=True)
    is_active = Column(Boolean, default=True)
    default_currency = Column(String(300), nullable=True)
    added_by =  Column(String(300), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
