# Inoffizielle API-Notizen

Diese Seite dokumentiert nur den derzeit nachvollziehbaren Kern der
SEMA-Python-Schnittstelle. Sie ist keine vollstaendige API-Referenz.

## Import

```python
from SEMAScripting import *
```

Der Sternimport ist in diesem Fall praktisch, weil neben
`SEMAScriptingManager` auch Konstanten wie `idUnDefined`, `dsAll`,
`ptTimber` und `stWall` benoetigt werden.

## Bauteile lesen

```python
parts = SEMAScriptingManager.GetData(idUnDefined, dsAll) or []
```

`GetData(objekt_ident, datenquelle)` liefert eine Liste von Bauteilen. Mit
`idUnDefined` wird nicht bereits nach einer bestimmten Identity gefiltert.
`dsAll` liest nach aktuellem Teststand projektweit.

Ein robuster Filter fuer alle Holzbauteile ist:

```python
timbers = [part for part in parts if part.PartType == ptTimber]
```

## Haeufig gelesene Eigenschaften

```python
part.Length
part.Width
part.Height
part.Designation
part.Annotation
part.Grade
part.Material
part.Free_1
part.PartType
part.StoType
part.Identity
```

Nicht jedes Objekt muss jede Eigenschaft besitzen. Fuer erkundende Skripte ist
deshalb `getattr(part, "Free_1", "")` sicherer als ein direkter Zugriff.

## Markieren

```python
changed = 0
for part in parts:
    if part.PartType == ptTimber:
        part.Marked = 1
        changed += 1

if changed:
    SEMAScriptingManager.UpdateParts()
```

Das Markieren und anschliessende Aktualisieren wurde praktisch bestaetigt.

## Dialoge

```python
SEMAScriptingManager.ShowMessage("Fertig")

value = SEMAScriptingManager.InputBox(
    "Mindestlaenge in Metern",
    "Holz markieren",
    "5.0",
)
```

`InputBox` liefert Text. Zahlen muessen selbst umgewandelt und auf Fehler
geprueft werden.

## Textfelder schreiben

Zuweisungen wie

```python
part.Free_1 = "stark"
```

sehen innerhalb desselben Skriptlaufs teilweise erfolgreich aus, wurden aus
dem allgemeinen Skript-Editor jedoch nicht dauerhaft in das SEMA-Modell
uebernommen. Dieses Muster wird daher hier nicht als funktionierende Loesung
empfohlen.
