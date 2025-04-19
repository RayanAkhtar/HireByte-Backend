import os
from dotenv import load_dotenv

env = os.getenv("ENVIRONMENT", "development")

if env == "production":
    load_dotenv(".env.production")
else:
    load_dotenv(".env.development")

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")
