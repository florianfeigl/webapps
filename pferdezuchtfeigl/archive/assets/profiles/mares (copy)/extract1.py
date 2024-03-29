import os
import yaml

# Definiere den Pfad zum Verzeichnis mit den Markdown-Dateien
verzeichnis_pfad = (
    "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares"
)
# Definiere den Pfad zur SQL-Datei
sql_datei_pfad = "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares/migration.sql"

# Öffne die SQL-Datei zum Schreiben (überschreibt die Datei, falls sie bereits existiert)
with open(sql_datei_pfad, "w") as sql_datei:
    # Iteriere über alle Dateien im angegebenen Verzeichnis
    for datei_name in os.listdir(verzeichnis_pfad):
        if datei_name.endswith(".md"):
            # Vollständiger Pfad zur aktuellen Markdown-Datei
            md_datei_pfad = os.path.join(verzeichnis_pfad, datei_name)

            # Lese den Inhalt der Markdown-Datei
            with open(md_datei_pfad, "r") as md_datei:
                inhalte = md_datei.read()
                # Versuche, den YAML-Header zu extrahieren
                try:
                    # Annahme: YAML-Header ist durch '---' vom Rest des Dokuments getrennt
                    yaml_header = inhalte.split("---")[1]
                    # Parse den YAML-Header
                    daten = yaml.safe_load(yaml_header)
                except Exception as e:
                    print(f"Fehler beim Verarbeiten von {datei_name}: {e}")
                    continue  # Bei einem Fehler, überspringe diese Datei und fahre mit der nächsten fort

                # Extrahiere die erforderlichen Daten
                name = daten.get("name", "Unbekannt")
                sex = daten.get("sex", "Unbekannt")
                birth = daten.get("birth", "Unbekannt")
                color = daten.get("color", "Unbekannt")
                region = daten.get("region", "Unbekannt")
                owner_id = daten.get("owner_id", "Unbekannt")
                breeder_id = daten.get("breeder_id", "Unbekannt")
                status = daten.get("status", "Unbekannt")

                # Erstelle das INSERT INTO-Statement
                insert_statement = f"INSERT INTO tabelle (name, sex, birth, color, region, owner_id, breeder_id, status) VALUES ('{name}', '{sex}', '{birth}', '{color}', '{region}', '{owner_id}', '{breeder_id}', '{status}');\n"

                # Schreibe das INSERT INTO-Statement in die SQL-Datei
                sql_datei.write(insert_statement)

print("SQL-Statements wurden erfolgreich erstellt.")
