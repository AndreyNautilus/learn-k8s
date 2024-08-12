"""Flask config"""

import os

BACKEND_ENDPOINT = os.getenv("BACKEND_ENDPOINT")
WORKER_NAME = os.getenv("WORKER_NAME", "Unknown worker")
