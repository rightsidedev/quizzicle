from flask import Flask

## Initialise Flask app and read config files
app = Flask(__name__)
from app import views
from dotenv import load_dotenv
import os

## Set up environment variables from applications .env file
APP_ROOT=os.path.join(os.path.dirname(__file__), "..") # application root dir
dotenv_path=os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)
