"""Liest freie Felder von Holzbauteilen, ohne das Modell zu veraendern."""

from SEMAScripting import *


MAX_EXAMPLES = 8
parts = SEMAScriptingManager.GetData(idUnDefined, dsAll) or []
timber_count = 0
with_free_1 = 0
examples = []

for part in parts:
    if part.PartType != ptTimber:
        continue

    timber_count += 1
    value = getattr(part, "Free_1", "")
    if value:
        with_free_1 += 1
        if len(examples) < MAX_EXAMPLES:
            designation = getattr(part, "Designation", "")
            examples.append(str(designation) + ": " + str(value))

lines = [
    "Holzbauteile: " + str(timber_count),
    "Davon mit Free_1: " + str(with_free_1),
]

if examples:
    lines.append("")
    lines.append("Beispiele:")
    lines.extend(examples)

SEMAScriptingManager.ShowMessage("\n".join(lines))
