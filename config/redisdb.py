import os
from walrus import *
from dotenv import load_dotenv

load_dotenv()

db = Database(host=os.getenv("host"), port=os.getenv("host"), db=0)

