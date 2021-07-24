import os
import nferx_py.fn as nf

from nferx_py.auth import HmacAuth
from pathlib import Path
from pymongo import MongoClient

# initialize local path
PATH = Path(os.path.dirname(os.path.abspath(__file__)))

# add nference API key
USER = 'krao@nference.net'
SECRET = '32ad1c0c62b498557a46099d65c6ddb8'
SERVER = 'preview'
nf.authenticate(USER, SECRET, server=SERVER)
nf.modify_defaults('logging', False)

MONGO_SERVER = 'mongo.servers.nferx.com'
MONGO_USER = 'krao'
MONGO_PASSWORD = 'QacGDvm9RMxp'

# initialize global authentication object
AUTH = HmacAuth(USER, SECRET)

client = MongoClient(MONGO_SERVER, username=MONGO_USER, password=MONGO_PASSWORD)