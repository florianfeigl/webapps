import os

import yaml

# Pfadangaben und weitere Details Ihrer Implementierung
# Definiere den Pfad zum Verzeichnis mit den Markdown-Dateien
verzeichnis_pfad = (
    "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares"
)
# Definiere den Pfad zur SQL-Datei
sql_datei_pfad = "/home/florian/Git/webapps/pferdezuchtfeigl/archive/assets/profiles/mares/migration.sql"

# Iteriere über alle Markdown-Dateien im Verzeichnis
for datei_name in os.listdir(verzeichnis_pfad):
    if datei_name.endswith(".md"):
        md_datei_pfad = os.path.join(verzeichnis_pfad, datei_name)
        with open(md_datei_pfad, "r") as md_datei:
            inhalte = md_datei.read()
            # Extrahiere den YAML-Header wie zuvor
            ...
            yaml_header = ...
            daten = yaml.safe_load(yaml_header)

            # Stellen Sie sicher, dass Sie jede Variable definieren, bevor Sie sie verwenden
            name = daten.get("name", "Unbekannt")
            sex = daten.get("sex", "Unbekannt")
            birth = daten.get("birth", "Unbekannt")
            color = daten.get("color", "Unbekannt")
            region = daten.get("region", "Unbekannt")
            owner_id = daten.get("owner_id", "Unbekannt")
            breeder_id = daten.get("breeder_id", "Unbekannt")
            status = daten.get("status", "Unbekannt")

            # Jetzt ist sichergestellt, dass `name` (und alle anderen Variablen) definiert sind
            insert_statement = f"INSERT INTO tabelle (name, sex, birth, color, region, owner_id, breeder_id, status) VALUES ('{name}', '{sex}', '{birth}', '{color}', '{region}', '{owner_id}', '{breeder_id}', '{status}');\n"

            # Füge das INSERT INTO-Statement in die SQL-Datei ein
            ...
