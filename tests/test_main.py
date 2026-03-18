import csv
import pytest
from src.main import process


def write_csv(path, rows):
    if not rows:
        path.write_text("")
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def test_process_keeps_rows_with_value(tmp_path):
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"
    write_csv(input_csv, [{"value": "42"}, {"value": "hello"}])

    process(str(input_csv), str(output_csv))

    result = read_csv(output_csv)
    assert result == [{"value": "42"}, {"value": "hello"}]


def test_process_filters_empty_string_value(tmp_path):
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"
    write_csv(input_csv, [{"value": "keep"}, {"value": ""}])

    process(str(input_csv), str(output_csv))

    result = read_csv(output_csv)
    assert len(result) == 1
    assert result[0]["value"] == "keep"


def test_process_filters_all_empty_values(tmp_path):
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"
    write_csv(input_csv, [{"value": ""}, {"value": ""}])

    process(str(input_csv), str(output_csv))

    assert output_csv.exists()
    result = read_csv(output_csv)
    assert result == []


def test_process_preserves_other_columns(tmp_path):
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"
    write_csv(input_csv, [
        {"id": "1", "value": "yes", "label": "a"},
        {"id": "2", "value": "",    "label": "b"},
    ])

    process(str(input_csv), str(output_csv))

    result = read_csv(output_csv)
    assert result == [{"id": "1", "value": "yes", "label": "a"}]


def test_process_mixed_rows(tmp_path):
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"
    rows = [
        {"value": "first"},
        {"value": ""},
        {"value": "second"},
        {"value": ""},
        {"value": "third"},
    ]
    write_csv(input_csv, rows)

    process(str(input_csv), str(output_csv))

    result = read_csv(output_csv)
    assert [r["value"] for r in result] == ["first", "second", "third"]
