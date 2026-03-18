import csv

def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def save_csv(data, path):
    if not data:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
