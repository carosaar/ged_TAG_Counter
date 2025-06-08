import sys
import csv
import os
from collections import defaultdict

def parse_gedcom(file_path):
    struktur_counts = defaultdict(lambda: defaultdict(int))
    l0_tags = set()
    current_l0_tag = None
    tag_stack = []

    with open(file_path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(" ", 2)
            if len(parts) < 2:
                continue

            try:
                level = int(parts[0])
            except ValueError:
                continue

            # L0: Zeiger und Tag extrahieren
            if level == 0:
                tag_stack = []
                if len(parts) == 3:
                    if parts[1].startswith("@") and parts[1].endswith("@"):
                        current_l0_tag = parts[2].split(" ")[0]
                    else:
                        current_l0_tag = parts[1]
                elif len(parts) == 2:
                    current_l0_tag = parts[1]
                else:
                    current_l0_tag = None

                if current_l0_tag:
                    l0_tags.add(current_l0_tag)
                continue

            if current_l0_tag is None:
                continue  # Sicherheitscheck

            # TAG extrahieren
            tag = parts[1]

            # Tag-Stack neu aufbauen ab Level 1 (L0 wird nicht gespeichert)
            if level == 1:
                tag_stack = [tag]
            elif level > 1:
                # Auffüllen oder Kürzen des Stacks
                if level <= len(tag_stack):
                    tag_stack = tag_stack[:level - 1]
                tag_stack.append(tag)

            struktur = ".".join(tag_stack)
            struktur_counts[struktur][current_l0_tag] += 1

    return struktur_counts, sorted(l0_tags)

def write_csv(output_path, struktur_counts, l0_tags):
    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["TAG-Struktur"] + l0_tags)

        for struktur in sorted(struktur_counts.keys()):
            row = [struktur]
            for tag in l0_tags:
                row.append(str(struktur_counts[struktur].get(tag, 0)))
            writer.writerow(row)

def main():
    if len(sys.argv) != 2:
        print("Verwendung: python ged_tag_counter.py <datei.ged>")
        sys.exit(1)

    gedcom_path = sys.argv[1]
    if not os.path.isfile(gedcom_path):
        print(f"Datei nicht gefunden: {gedcom_path}")
        sys.exit(1)

    print("GEDCOM-Datei wird analysiert...")
    struktur_counts, l0_tags = parse_gedcom(gedcom_path)

    output_csv = os.path.splitext(gedcom_path)[0] + "_tagstrukturen.csv"
    write_csv(output_csv, struktur_counts, l0_tags)
    print(f"Fertig\nCSV-Datei gespeichert unter: {output_csv}")

if __name__ == "__main__":
    main()
