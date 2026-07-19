# Aktueller Stand

Stand der Beobachtungen: Juli 2026, getestet mit `SEMA.DE_26.2.0.9`.

## Verifiziert

- `from SEMAScripting import *` stellt den Manager und SEMA-Konstanten bereit.
- `SEMAScriptingManager.GetData(...)` liefert iterierbare Bauteilobjekte.
- `GetData(idUnDefined, dsAll)` liest Bauteile projektweit.
- Holz kann mit `part.PartType == ptTimber` erkannt werden.
- Eigenschaften wie `Length`, `Designation`, `Grade` und `Free_1` sind lesbar.
- `part.Marked = 1` markiert ein Bauteil.
- `SEMAScriptingManager.UpdateParts()` macht die Markierung im Modell sichtbar.
- Meldungen lassen sich mit `SEMAScriptingManager.ShowMessage(...)` anzeigen.

## Beobachtet

Diese Datenquellen sind in der Python-Umgebung vorhanden:

| Konstante | Wert | Beobachtete Bedeutung |
|---|---:|---|
| `dsLikeF7` | 0 | Auswahl aehnlich F7 |
| `dsGraph` | 1 | aktuell aktive Zeichnung |
| `dsStorey` | 2 | aktuelles Geschoss |
| `dsAll` | 3 | gesamtes Projekt |
| `dsMarkable` | 4 | aktuell markierbare Bauteile |

Die genaue Reichweite kann vom aktiven SEMA-Kontext abhaengen. Insbesondere
`dsGraph` kann eine leere Liste liefern, wenn keine passende Zeichnung aktiv
ist.

## Offen oder widerlegt

- Das Schreiben von `Free_1`, `Pack` oder `Designation` blieb im allgemeinen
  Skript-Editor nicht dauerhaft erhalten.
- Auch ein fehlerfreier Lauf und `UpdateParts()` bestaetigen keinen
  Textfeld-Schreibzugriff.
- Vermutlich existiert fuer die Beschriftung ein besonderer Ausfuehrungskontext
  im ML-Bereich. Der genaue Einstiegspunkt ist noch unbekannt.
- Erzeugen, verschieben oder geometrisches Bearbeiten von Bauteilen ist noch
  nicht verifiziert.
