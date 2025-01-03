
from decimal import Decimal
from datetime import timedelta
import os

# Gold transformation constants
CLIENT_SHARE = Decimal('0.933')  # 93.3% client share
NETWORK_SHARE = Decimal('0.067')  # 6.7% network fee
STRUCTURE_FEE = Decimal('0.05')   # 5% structure fee

# Rate limiting defaults
DEFAULT_WINDOW_SIZE = 60  # seconds
DEFAULT_MAX_REQUESTS = 100

# Status codes as defined in GLOSSARY
STATUS_TO_BE_VERIFIED = 'to_be_verified'
STATUS_VERIFIED = 'verified'
STATUS_REJECTED = 'rejected'
STATUS_PENDING = 'pending'
STATUS_EXPIRED = 'expired'
STATUS_SUSPENDED = 'suspended'
STATUS_AVAILABLE = 'available'
STATUS_RESERVED = 'reserved'
STATUS_DISTRIBUTED = 'distributed'

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/gold_investment.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-change-in-production')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
