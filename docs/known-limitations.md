# Bekannte Grenzen

## Ausfuehrungskontext

Das Ergebnis von `GetData` haengt vom aktiven SEMA-Kontext ab. Ein Skript kann
fehlerfrei laufen und trotzdem keine Bauteile finden. `dsAll` ist fuer
projektweite Lese- und Markiervorgaenge bisher am verlaesslichsten.

## Textfelder

Direkte Zuweisung, `SetProps`, `SetValue` und `UpdateParts()` haben Textfelder
wie `Free_1`, `Pack` und `Designation` im allgemeinen Skript-Editor bisher
nicht dauerhaft gespeichert. Deshalb gibt es hier absichtlich kein Beispiel,
das einen funktionierenden Textfeld-Schreibzugriff verspricht.

## Signaturen

Einige Methoden stammen aus einer Delphi-Anbindung. Python-Introspektion zeigt
nicht immer eine brauchbare Signatur. Fehlermeldungen wie "Expected and actual
arguments are incompatible" bedeuten meist, dass Parameterart oder
Ausfuehrungskontext noch nicht bekannt sind.

## Geometrie und externe Module

Fuer das Erzeugen oder geometrische Veraendern von Bauteilen gibt es noch
keinen verifizierten Ablauf. Ebenso ist nicht geklaert, welche externen
Python-Pakete in verschiedenen SEMA-Installationen erlaubt sind. Beispiele in
diesem Repository verwenden deshalb nur Python und `SEMAScripting`.

## Versionen

Alle Aussagen koennen sich mit einer anderen SEMA-Version aendern. Ein Test in
einer Projektkopie bleibt notwendig.
