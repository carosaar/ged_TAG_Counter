# GEDCOM Tagstruktur-Zähler (`ged_tag_counter.py`)

Dieses Python-Skript analysiert eine GEDCOM-Datei (.ged) und zählt die vorkommenden TAG-Strukturen ab Ebene 1. Die Auswertung wird tabellarisch in einer CSV-Datei gespeichert, wobei pro oberstem Datensatztyp (z. B. INDI, FAM, NOTE, SOUR etc.) eine Spalte geführt wird.

## 🔍 Funktionsweise

Das Skript verarbeitet die Hierarchie der GEDCOM-TAGs ab Level 1. Dabei wird aus verschachtelten Einträgen eine Punktnotation gebildet, z. B.:

```gedcom
1 BIRT
2 DATE 12 JAN 1755
2 PLAC Saarbrücken
3 _LOC @L15399@
````

Ergibt folgende Strukturen:

* `BIRT`
* `BIRT.DATE`
* `BIRT.PLAC`
* `BIRT.PLAC._LOC`

Level-0-Zeilen (z. B. `0 @I123@ INDI`) werden nicht in die TAG-Struktur aufgenommen, sondern dienen zur Gruppierung nach Haupttypen (INDI, FAM, NOTE usw.).

## 📄 Ausgabe

Die Ausgabe ist eine CSV-Datei mit folgendem Aufbau:

| TAG-Struktur    | INDI | FAM | NOTE | ... |
| --------------- | ---- | --- | ---- | --- |
| NAME            | 1234 | 0   | 0    |     |
| NAME.GIVN       | 1200 | 0   | 0    |     |
| BIRT            | 1000 | 0   | 0    |     |
| BIRT.DATE       | 1000 | 0   | 0    |     |
| BIRT.PLAC       | 990  | 0   | 0    |     |
| BIRT.PLAC.\_LOC | 550  | 0   | 0    |     |
| ...             | ...  | ... | ...  |     |

Die CSV-Datei trägt denselben Namen wie die GEDCOM-Datei, jedoch mit dem Suffix `_tagstrukturen.csv`.

## ▶️ Verwendung

```bash
python ged_tag_counter.py <pfad/zur/datei.ged>
```

Beispiel:

```bash
python ged_tag_counter.py familienbuch.ged
```

Ergebnis:

```bash
GEDCOM-Datei wird analysiert...
Fertig
CSV-Datei gespeichert unter: familienbuch_tagstrukturen.csv
```

## ✅ Voraussetzungen

* Python 3.6 oder neuer
* Keine externen Bibliotheken notwendig

## 📁 Struktur

* `ged_tag_counter.py` – Hauptskript zur Analyse und CSV-Erzeugung
* Eingabe: GEDCOM-Datei (.ged)
* Ausgabe: CSV-Datei mit TAG-Strukturen und Häufigkeiten pro Datensatztyp

## 📝 Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](LICENSE) lizenziert.

---

**Autor**: Dieter Eckstein
**Version**: 1.0.0
