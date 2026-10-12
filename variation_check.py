import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python variation_check.py variation_audit_template.csv")
    raise SystemExit(1)

with open(sys.argv[1], newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

parents = {row["sku"] for row in rows if row.get("parentage") == "parent"}

for row in rows:
    if row.get("parentage") == "child":
        parent = (row.get("parent_sku") or "").strip()
        if not parent:
            print(f"{row['sku']}: missing parent SKU")
        elif parent not in parents:
            print(f"{row['sku']}: parent {parent} not found")

        if not (row.get("variation_theme") or "").strip():
            print(f"{row['sku']}: missing variation theme")
