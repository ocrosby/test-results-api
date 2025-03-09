import sys

from loguru import logger

# Remove default logger
logger.remove()

# Add a new logger with JSON format
logger.add(sys.stdout, format="{time} {level} {message}", serialize=True)
