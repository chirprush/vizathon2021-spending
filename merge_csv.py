#!/usr/bin/env python3
from collections import OrderedDict
from typing import Dict, Tuple, Optional, List, Any
import csv

State = str

def to_rows(state_attrs: Dict[State, Dict[str, str]]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for state, data in state_attrs.items():
        row: Dict[str, str] = {**data, "state" : state}
        rows.append(row)
    return rows

state_data: Dict[State, Dict[str, Any]] = {}

with open("spending.csv", newline="") as spending_file, open("cases.csv", newline="") as cases_file:
    cases_data = csv.DictReader(cases_file)
    for row in cases_data:
        state = row["State"]
        if state in state_data:
            state_data[state]["cases"] += int(row["2021-07-29"])
        else:
            state_data[state] = {"cases" : int(row["2021-07-29"])}
    spending_data = csv.DictReader(spending_file)
    for row in spending_data:
        state = row["state"]
        total = row["total"]
        tpc = row["tpc"]
        state_data[state].update({"total" : total, "tpc" : tpc})

with open("merged.csv", "w", newline="") as merged_file:
    fieldnames = ["state", "total", "tpc", "cases"]
    writer: csv.DictWriter = csv.DictWriter(merged_file, fieldnames=fieldnames)
    writer.writeheader()
    state_rows: List[Dict[str, str]] = to_rows(state_data)
    for state_row in state_rows:
        writer.writerow(state_row)
