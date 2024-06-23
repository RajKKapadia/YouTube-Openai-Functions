import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_MODEL = os.getenv('GPT_MODEL')

TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
TWILIO_SID = os.getenv('TWILIO_SID')
FROM = os.getenv('FROM')

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

ERROR_MESSAGE = 'We are facing an issue, please try after sometimes.'
