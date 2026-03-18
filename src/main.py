import argparse
from utils import load_csv, save_csv
from config import DEFAULT_INPUT, DEFAULT_OUTPUT

def process(input_path, output_path):
    data = load_csv(input_path)
    cleaned = [row for row in data if row.get("value")]
    save_csv(cleaned, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    process(args.input, args.output)
