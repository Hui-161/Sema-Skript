"""Erstellt einen rein lesenden Kurzbericht zur aktiven SEMA-Umgebung."""

import sys

from SEMAScripting import *


lines = [
    "SEMA Python-Umgebung",
    "Python: " + sys.version.replace("\n", " "),
]

data_sources = [
    ("dsLikeF7", globals().get("dsLikeF7")),
    ("dsGraph", globals().get("dsGraph")),
    ("dsStorey", globals().get("dsStorey")),
    ("dsAll", globals().get("dsAll")),
    ("dsMarkable", globals().get("dsMarkable")),
]

for name, source in data_sources:
    if source is None:
        lines.append(name + ": nicht vorhanden")
        continue

    try:
        parts = SEMAScriptingManager.GetData(idUnDefined, source) or []
        timber_count = sum(
            1 for part in parts if getattr(part, "PartType", None) == ptTimber
        )
        lines.append(
            name
            + "="
            + str(source)
            + ": "
            + str(len(parts))
            + " Bauteile, "
            + str(timber_count)
            + " Holz"
        )
    except Exception as error:
        lines.append(name + ": " + type(error).__name__ + ": " + str(error))

report = "\n".join(lines)
print(report)
SEMAScriptingManager.ShowMessage(report)
