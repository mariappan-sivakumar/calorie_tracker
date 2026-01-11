import logging
import sys


def setup_logging():
    # Clear all existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler.setFormatter(formatter)

    # Attach handler to root logger
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(console_handler)
