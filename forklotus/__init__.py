# forklotus/__init__.py

import requests

session = requests.Session()

from .wf_api import *
from .worldstate_classes import *
from .query_classes import *
from .exceptions import *