#!/bin/zsh

# Pfad zum Verzeichnis mit den Markdown-Dateien
verzeichnis_pfad='/pfad/zu/deinem/verzeichnis'
# Pfad zur SQL-Datei
sql_datei_pfad='/pfad/zu/deiner/datei.sql'

# Leere die SQL-Datei zu Beginn
> $sql_datei_pfad

# Iteriere über alle Markdown-Dateien
for md_datei in "$verzeichnis_pfad"/*.md; do
  # Extrahiere den YAML-Header
  yaml_header=$(sed -n '/^---$/,/^---$/p' "$md_datei" | sed '1d;$d')
  
  # Extrahiere Titel und Datum
  titel=$(echo "$yaml_header" | grep 'title:' | cut -d ':' -f2 | xargs)
  datum=$(echo "$yaml_header" | grep 'date:' | cut -d ':' -f2 | xargs)
  
  # Erstelle das INSERT INTO-Statement
  echo "INSERT INTO tabelle (titel, datum) VALUES ('$titel', '$datum');" >> $sql_datei_pfad
done

echo "SQL-Statements wurden erfolgreich erstellt und in $sql_datei_pfad gespeichert."

