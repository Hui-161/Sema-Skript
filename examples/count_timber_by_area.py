"""Zaehlt Holzbauteile nach Wand, Decke, Dach und sonstigem Bereich."""

from SEMAScripting import *


parts = SEMAScriptingManager.GetData(idUnDefined, dsAll) or []
counts = {
    "Wand": 0,
    "Decke": 0,
    "Dach": 0,
    "Sonstige": 0,
}

for part in parts:
    if part.PartType != ptTimber:
        continue

    if part.StoType == stWall:
        counts["Wand"] += 1
    elif part.StoType == stCeiling:
        counts["Decke"] += 1
    elif part.StoType == stRoof:
        counts["Dach"] += 1
    else:
        counts["Sonstige"] += 1

message = "\n".join(
    [
        "Holzbauteile im Projekt:",
        "Wand: " + str(counts["Wand"]),
        "Decke: " + str(counts["Decke"]),
        "Dach: " + str(counts["Dach"]),
        "Sonstige: " + str(counts["Sonstige"]),
    ]
)
SEMAScriptingManager.ShowMessage(message)
