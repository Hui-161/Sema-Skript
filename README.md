# SEMA Python-Skripte

Eine kleine, inoffizielle Sammlung von nachvollziehbaren Erkenntnissen und
Beispielen zur Python-Schnittstelle von SEMA.

Die Schnittstelle ist noch wenig dokumentiert. Deshalb trennt dieses Repository
streng zwischen:

- **verifiziert**: in SEMA praktisch getestet,
- **beobachtet**: vorhanden, aber noch nicht ausreichend getestet,
- **offen**: Wirkung oder richtiger Aufruf sind noch unklar.

## Teststand

| Umgebung | Stand |
|---|---|
| SEMA | `SEMA.DE_26.2.0.9` |
| Python in SEMA | 3.13 |
| Bauteile lesen | verifiziert |
| Bauteile filtern und zaehlen | verifiziert |
| Bauteile markieren | verifiziert |
| Textfelder wie `Free_1` schreiben | im allgemeinen Skript-Editor nicht dauerhaft |
| Geometrie erzeugen oder veraendern | nicht verifiziert |

Der Teststand bezieht sich auf die genannte Version. Andere SEMA-Versionen
koennen sich anders verhalten.

## Schnellstart

1. In SEMA den Python-Skript-Editor oeffnen.
2. Ein Skript aus [`examples/`](examples/) kopieren.
3. Das Skript zuerst in einem Testprojekt ausfuehren.
4. Ergebnis und SEMA-Version dokumentieren, wenn sich das Verhalten unterscheidet.

Ein bewusst kleines Beispiel:

```python
from SEMAScripting import *

parts = SEMAScriptingManager.GetData(idUnDefined, dsAll) or []
for part in parts:
    if part.PartType == ptTimber and part.Length > 5.0:
        part.Marked = 1

SEMAScriptingManager.UpdateParts()
```

## Inhalt

- [`docs/status.md`](docs/status.md): was aktuell als bestaetigt gilt
- [`docs/api-reference.md`](docs/api-reference.md): kompakte API-Notizen
- [`docs/known-limitations.md`](docs/known-limitations.md): bekannte Grenzen
- [`examples/`](examples/): kleine, einzeln ausfuehrbare Skripte
- [`diagnostics/environment_report.py`](diagnostics/environment_report.py):
  rein lesende Umgebungsdiagnose
- [`CONTRIBUTING.md`](CONTRIBUTING.md): Beobachtungen reproduzierbar teilen

## Wichtiger Hinweis

Dieses Projekt ist weder von SEMA autorisiert noch eine offizielle
Dokumentation. Skripte koennen Projektdaten veraendern. Vor Schreibversuchen
immer mit einer Projektkopie arbeiten.

Logs, Projektdateien, Kundendaten und nicht reproduzierbare Experimente gehoeren
nicht in dieses oeffentliche Repository. Der aktuelle Forschungsstand wird
bewusst nur in kleinen, geprueften Schritten uebernommen.
