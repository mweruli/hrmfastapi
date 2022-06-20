
from fastapi import FastAPI
from pydantic import BaseModel


class Company(BaseModel):
    name: str
    trading_name: str
    registration_no: str
    government_tax: str
    email: str
    contact_number: str
    address_1: str
    city: str
    state: str
    is_active: bool
    default_currency: str
