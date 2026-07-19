"""Markiert alle Holzbauteile, die laenger als der Grenzwert sind."""

from SEMAScripting import *


MIN_LENGTH_M = 5.0

parts = SEMAScriptingManager.GetData(idUnDefined, dsAll) or []
marked_count = 0

for part in parts:
    if part.PartType == ptTimber and part.Length > MIN_LENGTH_M:
        part.Marked = 1
        marked_count += 1

if marked_count:
    SEMAScriptingManager.UpdateParts()

SEMAScriptingManager.ShowMessage(
    str(marked_count)
    + " Holzbauteile ueber "
    + str(MIN_LENGTH_M)
    + " m wurden markiert."
)
