"""Flask config"""

import os

BACKEND_ENDPOINT = os.getenv("BACKEND_ENDPOINT")
BACKEND_SECRET = os.getenv("BACKEND_SECRET", "anonymous")
WORKER_NAME = os.getenv("WORKER_NAME", "Unknown worker")
