import os

# Connection details for a Business Central OData endpoint, read from the environment.
BASE_URL = os.environ.get("BC_BASE_URL", "http://localhost:7048")
PATH = os.environ.get("BC_PATH", "/bc210/ODataV4/Company('CRONUS International Ltd.')/webservices/")
USER = os.environ.get("BC_USER", "")
PASSWORD = os.environ.get("BC_PASSWORD", "")
PARAM = os.environ.get("BC_PARAM", "")
