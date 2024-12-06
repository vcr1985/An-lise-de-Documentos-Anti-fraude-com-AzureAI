import os
from dotenv import load_dotenv
load_dotenv()

class config:
    ENDPOINT = os.getenv("ENDPOINT") 
SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME") 