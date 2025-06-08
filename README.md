# GEDCOM Tagstruktur-Zähler (`ged_tag_counter.py`)

Dieses Python-Skript analysiert eine GEDCOM-Datei (.ged) und zählt die vorkommenden TAG-Strukturen ab Ebene 1. Die Auswertung wird tabellarisch in einer CSV-Datei gespeichert, wobei pro oberstem Datensatztyp (z. B. INDI, FAM, NOTE, SOUR etc.) eine Spalte geführt wird.

## **drei typische Einsatzbereiche** 

### 🛠️ **Einsatzbereich 1: Strukturvalidierung von GEDCOM-Dateien**

**Analyseergebnis:**
Du kannst **fehlerhafte oder ungewöhnliche TAG-Strukturen** leicht erkennen – z. B. wenn:

* ein Untertag an einer falschen Stelle auftaucht (z. B. `SEX.DATE`, was keinen Sinn ergibt),
* ein Level übersprungen wurde (z. B. direkt von `1 BIRT` zu `3 DATE` ohne `2 DATE`),
* ein TAG mehrfach verschachtelt vorkommt, obwohl es nur einfach erlaubt ist (z. B. `RELI.RELI`).

➡ **Nutzen:** Das hilft bei der Qualitätskontrolle genealogischer Daten oder bei der Fehlersuche in GEDCOM-Dateien aus unterschiedlichen Quellen.

### 🗂️ **Einsatzbereich 2: Überblick über die Datenstruktur einer GEDCOM-Datei**

**Analyseergebnis:**
Die Datei liefert einen **kompakten Überblick darüber**, welche TAGs (und Untertags) in welcher Häufigkeit bei welchen **L0-Datensatztypen** vorkommen (z. B. INDI, FAM, NOTE).

➡ **Nutzen:** So erkennst du z. B., ob ein bestimmter TAG wie `BIRT.PLAC` bei fast allen INDI-Datensätzen vorhanden ist – oder ob bestimmte Felder fast nie befüllt sind (z. B. `FACT.NOTE` nur bei wenigen Personen).

### 🧬 **Einsatzbereich 3: Vorbereitung für Datenextraktion und Weiterverarbeitung**

**Analyseergebnis:**
Die CSV-Ausgabe zeigt dir, **welche Daten sich systematisch extrahieren lassen**, da sie regelmäßig in strukturierter Form vorkommen – z. B.:

* `BIRT.DATE` → ideal zur Ermittlung von Geburtsjahrgängen,
* `CHR.PLAC` → gut für Tauf-Ortsanalysen,
* `FACT.TYPE` + `FACT.NOTE` → zur Auswertung spezieller Ereignisse oder Kennzeichnungen.

➡ **Nutzen:** Das hilft bei der Entwicklung eigener Tools zur Auswertung, Visualisierung oder Migration genealogischer Daten.

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
