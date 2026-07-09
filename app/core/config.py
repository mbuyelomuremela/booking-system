from dotenv import load_dotenv
import os

# loading environment variables
load_dotenv()

DATABASE_URI = os.environ.get("DATABASE_URI")
SECRET_KEY = os.environ.get("SECRET_KEY")

