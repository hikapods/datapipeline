import csv
import logging

logger = logging.getLogger(__name__)

def load_csv(path):
    try:
        with open(path, newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        logger.error("CSV file not found: %s", path)
        raise
    except PermissionError:
        logger.error("Permission denied reading file: %s", path)
        raise
    except csv.Error as e:
        logger.error("Failed to parse CSV file %s: %s", path, e)
        raise

def save_csv(data, path, fieldnames=None):
    if fieldnames is None:
        if not data:
            return
        fieldnames = list(data[0].keys())
    try:
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except PermissionError:
        logger.error("Permission denied writing file: %s", path)
        raise
    except OSError as e:
        logger.error("Failed to write CSV file %s: %s", path, e)
        raise
