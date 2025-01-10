"""Flask config"""

import os

DEFAULT_WORKER_NAME = "Unknown worker"

WORKER_NAME = os.getenv("WORKER_NAME", DEFAULT_WORKER_NAME)
