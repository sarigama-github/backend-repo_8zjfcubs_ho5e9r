"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# Example schemas (you can keep or remove if not needed):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: Optional[str] = Field(None, description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Smylor Dental Care Schemas

class Appointment(BaseModel):
    """
    Appointment requests for Smylor Dental Care
    Collection name: "appointment"
    """
    full_name: str = Field(..., description="Patient full name")
    email: EmailStr = Field(..., description="Patient email")
    phone: str = Field(..., description="Contact phone number")
    preferred_date: Optional[str] = Field(None, description="Preferred date (YYYY-MM-DD)")
    preferred_time: Optional[str] = Field(None, description="Preferred time (e.g., 10:30 AM)")
    service: Optional[str] = Field(None, description="Requested service")
    notes: Optional[str] = Field(None, description="Additional notes")
    source: str = Field("website", description="Source of request")

class ContactMessage(BaseModel):
    """
    General contact messages
    Collection name: "contactmessage"
    """
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    subject: Optional[str] = Field(None, description="Message subject")
    message: str = Field(..., description="Message body")
    sent_at: Optional[datetime] = Field(None, description="Client timestamp if provided")

# Note: The Flames database viewer can read these via a /schema endpoint if provided.
