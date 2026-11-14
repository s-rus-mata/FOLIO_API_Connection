import os
import requests
import json
import asyncio
from connection import Connection
import asyncio
from dotenv import load_dotenv
from pymarc import MARCReader, MARCWriter

load_dotenv("private.env")

API_URL = os.getenv("API_URL")
API_TENANT = os.getenv("API_TENANT")
TOKEN = asyncio.run(Connection().get_token())

HEADERS = {
    'x-okapi-token': TOKEN,
    'x-okapi-tenant': API_TENANT,
    'Content-Type': 'application/json'
}

