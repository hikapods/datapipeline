import argparse
import logging
from utils import load_csv, save_csv
from config import DEFAULT_INPUT, DEFAULT_OUTPUT, LOG_LEVEL

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)

def process(input_path, output_path):
    data = load_csv(input_path)
    fieldnames = list(data[0].keys()) if data else None
    cleaned = [row for row in data if row.get("value")]
    save_csv(cleaned, output_path, fieldnames=fieldnames)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    process(args.input, args.output)
