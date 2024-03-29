import os

import yaml

# Definiere den Pfad zum Verzeichnis mit den Markdown-Dateien
verzeichnis_pfad = (
    "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares"
)
# Definiere den Pfad zur SQL-Datei
sql_datei_pfad = "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares/migration.sql"

# Öffne die SQL-Datei im Append-Modus
with open(sql_datei_pfad, "a") as sql_datei:
    # Iteriere über alle Dateien im Verzeichnis
    for datei_name in os.listdir(verzeichnis_pfad):
        if datei_name.endswith(".md"):
            # Vollständiger Pfad zur Markdown-Datei
            md_datei_pfad = os.path.join(verzeichnis_pfad, datei_name)
            # Lese den Inhalt der Markdown-Datei
            with open(md_datei_pfad, "r") as md_datei:
                inhalte = md_datei.read()
                # Extrahiere den YAML-Header
                yaml_header = inhalte.split("---")[1]

                # Ersetze Tabs durch Leerzeichen im YAML-Header
                yaml_header = yaml_header.replace(
                    "\t", "  "
                )  # Ersetzt jeden Tab durch zwei Leerzeichen

                # Parse den YAML-Header zu einem Python-Dict
                daten = yaml.safe_load(yaml_header)
                # Extrahiere die gewünschten Parameter (Beispielparameter)
                param1 = daten.get("name", "default")
                param2 = daten.get("sex", "default")
                param1 = daten.get("birth", "default")
                param2 = daten.get("color", "default")
                param2 = daten.get("region", "default")
                param1 = daten.get("owner_id", "default")
                param2 = daten.get("breeder_id", "default")
                param2 = daten.get("status", "default")
                # ... Füge hier Extraktion für weitere Parameter hinzu ...

                # Erstelle das INSERT INTO-Statement
                insert_statement = f"INSERT INTO tabelle (name, sex, birth, color, region, owner_id, breeder_id, status) VALUES ('{name}', '{sex}', '{birth}', '{color}', '{region}', '{owner_id}', '{breeder_id}', '{status}');\n"
                # ... Ergänze das Statement um weitere Parameter ...

                # Schreibe das INSERT INTO-Statement in die SQL-Datei
                sql_datei.write(insert_statement)
