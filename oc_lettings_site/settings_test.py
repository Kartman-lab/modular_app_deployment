from pathlib import Path
from dotenv import load_dotenv
import os

from oc_lettings_site.settings import *

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")

ROOT_URLCONF = "oc_lettings_site.urls"

# Base de données en mémoire pour tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

DEBUG = False
